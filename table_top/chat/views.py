from django.db.models.query import QuerySet
from django.http import response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Chat
from .serializers import ChatSerializer
from django.contrib.auth.models import User


@api_view(['GET'])
@permission_classes ([AllowAny])
def get_all_chat(request):
    chat = Chat.objects.all()
    serializer = ChatSerializer(chat, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes ([AllowAny])
def get_chat(request):
        chat = Chat.objects.get(id)
        serializer = ChatSerializer(chat, many=True)
        return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes ([AllowAny])
def delete(request):
        chat = Chat.objects.delete(id)
        chat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes ([AllowAny])
def post_chat(request):
    if request.method == 'POST':
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response (serializer.data, status=status.HTTP_204_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)