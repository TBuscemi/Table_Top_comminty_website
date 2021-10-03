from rest_framework import serializers
from .models import Account
from django.http import Http404
from django.contrib.auth.models import User

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['user','discord','platform_played_on','game_systems_looking_for','campaign_length','player','gm','looking_for_game','party_leaders','chat_name']
     

        def getUser(self, uid):
            try:
                return User.objects.get(id=uid)
            except Account.DoesNotExist:
                raise Http404    

        def update(self, account, validated_data):
            # account = Account.objects.get(user_id = validated_data['user'])
                
            account.discord=validated_data['discord']
            account.platform_played_on=validated_data['platform_played_on']
            account.game_systems_looking_for=validated_data['game_systems_looking_for']
            account.campaign_length=validated_data['campaign_length']
            account.player=validated_data['player']
            account.gm=validated_data['gm']
            account.looking_for_game=validated_data['looking_for_game']
            account.party_leaders=validated_data['party_leaders']
            account.chat_name=validated_data['chat_name']
            
            account.save()

            return account
        
        def create(self, validated_data):
            account = Account.objects.create(
            user=validated_data['username'])
            account.save
