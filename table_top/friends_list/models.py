from django.db import models


class FriendsList(models.Model):
    friends = models.CharField(max_length=200)
    friends_status = models.BooleanField

