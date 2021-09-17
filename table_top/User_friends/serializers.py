from rest_framework import serializers
from .models import UserFriends

class UserFriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFriends
        fields = ['user','friendslist']
     
