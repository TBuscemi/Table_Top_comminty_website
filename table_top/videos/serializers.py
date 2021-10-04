from rest_framework import serializers
from .models import Videos
from django.http import Http404


class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = ['dungeon_and_dragons','pathfinder','roll20','fantasy_grounds']
     
    def update(self, videos, validated_data):
           
            videos.dungeon_and_dragons=validated_data['dungeon_and_dragons']
            videos.pathfinder=validated_data['pathfinder']
            videos.roll20=validated_data['roll20']
            videos.fantasy_grounds=validated_data['fantasy_grounds']
            
            
            videos.save()

            return videos
  