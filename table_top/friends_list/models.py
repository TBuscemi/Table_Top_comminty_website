from django.db import models
from django.contrib.auth.modles import User

class FriendsList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friends = models.CharField(max_length=200)
    friends_status = models.BooleanField

