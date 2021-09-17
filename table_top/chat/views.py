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
def get_all_accounts(request):
    accounts = Chat.objects.all()
    serializer = ChatSerializer(accounts, many=True)
    return Response(serializer.data)

