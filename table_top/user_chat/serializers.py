from rest_framework import serializers
from .models import UserChat

class UserChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChat
        fields = ['user','chat']
     
