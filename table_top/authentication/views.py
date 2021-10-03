from django.contrib.auth.models import User
from django.contrib.auth.models import User
from .serializers import RegistrationSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.http import Http404
from authentication import serializers



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permissions_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    
    
    
class UserPostGet(APIView):
    
    
    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response (status = 404)

    def get(self, request, pk):
        user = self.get_user(pk=pk)
        serializer = RegistrationSerializer(user)
        return Response(serializer.data)

    def put(self,request, pk):
        user = self.get_user(pk=pk)
        serializer = RegistrationSerializer(user, data=request.data)
        if  serializer.is_valid():    
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)