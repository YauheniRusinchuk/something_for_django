from django.db import models
from django.contrib.auth import get_user_model
#from src.models.twit.models import Twit

User = get_user_model()

class Profile(models.Model):

    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    login       = models.CharField(max_length=255, blank=False)
    followers   = models.ManyToManyField("Profile", related_name='flwrs')


    def __str__(self):
        return f"{self.login}"


    def twits_my_followers(self):
        return self.followers.all()
        #twits_followers = Twit.objects.filter(profile__in=followrs_this_profile)
