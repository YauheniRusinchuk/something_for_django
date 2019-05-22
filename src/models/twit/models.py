from django.db import models
from src.models.profile.models import Profile

class Twit(models.Model):
    
    profile     = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text        = models.TextField(blank=False)


    def __str__(self):
        return f"It's twit {self.profile.user}"
