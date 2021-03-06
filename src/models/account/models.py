from django.db import models
from src.apps.tasks.task import get_email
# Create your models here.
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Email is required...")
        if not password:
            raise ValueError("Password is required...")
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.active = is_active
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.save(using=self._db)
        return user_obj

    def create_stuffuser(self, email, password=None):
        user = self.create_user(
            email,
            password = password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password = password,
            is_staff=True,
            is_admin=True
        )
        return user




class User(AbstractBaseUser):
    email   = models.EmailField(max_length=255, unique=True)
    active  = models.BooleanField(default=True)
    staff   = models.BooleanField(default=False)
    admin   = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []

    objects = UserManager()

    def __str__(self):
        return f"Email is {self.email}"


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


from django.db.models import signals


def user_post_save(sender, instance, signal, *args, **kwargs):
    if instance:
        get_email.delay(instance.email)

signals.post_save.connect(user_post_save, sender=User)
