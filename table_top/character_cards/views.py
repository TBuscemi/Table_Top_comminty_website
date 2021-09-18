from django.db.models.query import QuerySet
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import CharacterCards
from .serializers import CharacterCardsSerializer
from django.contrib.auth.models import User

@api_view(['GET'])
@permission_classes ([AllowAny])
def get_all_character_cards(request):
    cards = CharacterCards.objects.all()
    serializer = CharacterCardsSerializer(cards, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes ([AllowAny])
def get_character_cards(request):
        cards = CharacterCards.objects.get(id)
        serializer = CharacterCardsSerializer(cards, many=True)
        return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes ([AllowAny])
def delete(request):
        cards = CharacterCards.objects.get(id)
        cards.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes ([AllowAny])
def post_character_cards(request):
    if request.method == 'POST':
        serializer = CharacterCardsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response (serializer.data, status=status.HTTP_204_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)