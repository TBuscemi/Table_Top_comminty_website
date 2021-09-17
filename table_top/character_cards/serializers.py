from rest_framework import serializers
from .models import CharacterCards

class CharacterCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterCards
        fields = ['user','character_name','character_description','character_image']
     