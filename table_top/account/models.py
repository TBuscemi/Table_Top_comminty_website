from django.db import models
from django.contrib.auth.modles import User

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discord = models.CharField(max_length=50)
    platform_played_on = models.CharField(max_length=200)
    game_systems_looking_for = models.CharField(max_length=200)
    campaign_length = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    player = models.BooleanField
    gm = models.BooleanField