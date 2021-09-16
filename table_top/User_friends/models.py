from table_top.friends_list.models import FriendsList
from django.db import models
from django.contrib.auth.modles import User
from friends_list import FriendsList

class UserFriends(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friendslist = models.ForeignKey(FriendsList, on_delete=models.CASCADE)