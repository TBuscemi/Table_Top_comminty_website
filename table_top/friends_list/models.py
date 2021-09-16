from django.db import models
from django.contrib.auth.modles import User

class FriendsList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friends_list = models.CharField(max_length=1000)
    friends_status = models.BooleanField