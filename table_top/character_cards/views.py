from django.db.models.query import QuerySet
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import CharacterCards
from .serializers import CharacterCardsSerializer
from django.contrib.auth.models import User

class CharacterCardsList(APIView):
    
    permission_classes = [AllowAny]
  
    def get(self, request):
        Card = CharacterCards.objects.all()
        serializer = CharacterCardsSerializer(Card, many=True)
        return Response(serializer.data)
        