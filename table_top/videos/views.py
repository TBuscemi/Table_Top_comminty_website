from django.http import response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Videos
from .serializers import VideosSerializer
from django.http import Http404
from videos import serializers



class Videos_tutorials(APIView):

    def get_vid(self, pk):
        try:
            return Videos.objects.get(pk=pk)
        except Videos.DoesNotExist:
            raise Http404

    def get(self, request, pk):
            video = self.get_vid(pk)
            serializer = VideosSerializer(video)
            return Response(serializer.data)

    def put(self,request, pk):
        video = self.get_vid(pk)
        serializer = VideosSerializer(video, data=request.data)
        if  serializer.is_valid():    
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = VideosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)