from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model
#from src.models.twit.models import Twit

User = get_user_model()

class Profile(models.Model):

    slug        = models.SlugField()
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    login       = models.CharField(max_length=255, blank=False)
    followers   = models.ManyToManyField("Profile", related_name='flwrs')
    avatar      = models.ImageField(upload_to='avatar/', blank=True)


    def __str__(self):
        return f"{self.login}"



def pre_save_profile_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.login)
    instance.slug = slug
    # if not instance.img:
    #      return False
    # old_file = sender.objects.get(user=instance.user).img or None
    #
    # if old_file:
    #     if not old_file == instance.img:
    #         if os.path.isfile(old_file.path):
    #             os.remove(old_file.path)



pre_save.connect(pre_save_profile_receiver, sender=Profile)
