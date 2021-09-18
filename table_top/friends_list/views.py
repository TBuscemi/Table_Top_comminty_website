from django.db.models.query import QuerySet
from django.http import response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import FriendsList
from .serializers import FriendsListSerializer
from django.contrib.auth.models import User


@api_view(['GET'])
@permission_classes ([AllowAny])
def get_all_friends_list(request):
    chat = FriendsList.objects.all()
    serializer = FriendsListSerializer(chat, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes ([AllowAny])
def get_friends_list(request):
        chat = FriendsList.objects.get(id)
        serializer = FriendsListSerializer(chat, many=True)
        return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes ([AllowAny])
def delete(request):
        chat = FriendsList.objects.delete(id)
        chat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes ([AllowAny])
def post_friends_list(request):
    if request.method == 'POST':
        serializer = FriendsListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response (serializer.data, status=status.HTTP_204_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)