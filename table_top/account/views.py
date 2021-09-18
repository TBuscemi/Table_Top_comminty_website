from django.db.models.query import QuerySet
from django.http import response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Account
from .serializers import AccountSerializer
from django.contrib.auth.models import User


    

@api_view(['GET'])
@permission_classes ([AllowAny])
def get_all_accounts(request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes ([AllowAny])
def get_account(request):
        accounts = Account.objects.get(id)
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes ([AllowAny])
def delete(request):
        accounts = Account.objects.delete(id)
        accounts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes ([AllowAny])
def post_user(request):
    if request.method == 'POST':
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response (serializer.data, status=status.HTTP_204_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)