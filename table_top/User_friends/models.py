from django.db import models
from django.contrib.auth.models import User
from friends_list.models import FriendsList

class UserFriends(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friendslist = models.ForeignKey(FriendsList, on_delete=models.CASCADE)