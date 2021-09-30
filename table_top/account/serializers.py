from rest_framework import serializers
from .models import Account
from django.http import Http404
from django.contrib.auth.models import User

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['user','discord','platform_played_on','game_systems_looking_for','campaign_length','description','player','gm','looking_for_game']
     

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
            account.description=validated_data['description']
            account.player=validated_data['player']
            account.gm=validated_data['gm']
            account.looking_for_game=validated_data['looking_for_game']
            
            account.save()

            return account
