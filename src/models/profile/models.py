from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Profile(models.Model):

    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    login       = models.CharField(max_length=255, blank=False)
    


    def __str__(self):
        return f"{self.login}"
