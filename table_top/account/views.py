from django.contrib.auth.models import User
import account
from django.http import response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Account
from .serializers import AccountSerializer
from django.http import Http404
from account import serializers


    

# @api_view(['GET'])
# @permission_classes ([AllowAny])
# def get_all_accounts(request):
#     accounts = Account.objects.all()
#     serializer = AccountSerializer(accounts, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# @permission_classes ([AllowAny])
# def get_account(request):
#         accounts = Account.objects.get(id)
#         serializer = AccountSerializer(accounts, many=True)
#         return Response(serializer.data)


# @api_view(['DELETE'])
# @permission_classes ([AllowAny])
# def delete(request):
#         accounts = Account.objects.delete(id)
#         accounts.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['POST'])
# @permission_classes ([AllowAny])
# def post_user(request):
#     if request.method == 'POST':
#         serializer = AccountSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response (serializer.data, status=status.HTTP_204_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class Accounts_Get(APIView):
    
    def get(self, request):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)
                                                                                                                                                                                                                                                                                                                                                    
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Account_Query(APIView):

    def get_account(self, pk):
        try:
            return Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        account = self.get_account(pk)
        serializer = AccountSerializer(account)
        return Response(serializer.data)

class Account_By_User(APIView):

    def get_account(self, uid):
        try:
            return Account.objects.get(user=uid)
        except Account.DoesNotExist:
            raise Http404


    def get(self, request, uid):
        account = self.get_account(uid)
        serializer = AccountSerializer(account)
        return Response(serializer.data)

    def put(self, request, uid):
        account = self.get_account(uid)
        # request.data['user'] = serializer 
        serializer = AccountSerializer(account, data=request.data)
        serializer.update(account, request.data)
        return Response(serializer.data)
        
class Account_Search (APIView):
    
    def post(self,request):
        criteria = Account.objects.all()
        if request.data['platform_played_on'] is not '':
            criteria = criteria.filter(platform_played_on = request.data['platform_played_on'])
        if request.data['game_systems_looking_for'] is not '':
            criteria = criteria.filter(game_systems_looking_for = request.data['game_systems_looking_for'])
        if request.data['campaign_length'] is not '':
            criteria = criteria.filter(campaign_length = request.data['campaign_length'])
        if request.data['player'] is not '':
            criteria = criteria.filter(player = request.data['player'])
        if request.data['gm'] is not '':
            criteria = criteria.filter(gm = request.data['gm'])
        if request.data['looking_for_game'] is not '':
            criteria = criteria.filter(gm = request.data['looking_for_game'])
        serializer = AccountSerializer(criteria, many = True)
        return Response(serializer.data)

        
        



        # fields = ['discord','platform_played_on','game_systems_looking_for','campaign_length','description','player','gm']