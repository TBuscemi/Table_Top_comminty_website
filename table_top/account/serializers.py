from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['user','discord','platform_played_on','game_systems_looking_for','campaign_length','description','player','gm']
     



        