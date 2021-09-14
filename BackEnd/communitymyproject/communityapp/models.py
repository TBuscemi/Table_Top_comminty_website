from django.db import models
from django.db.models.fields import EmailField


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    discord = models.CharField(max_length=50)
    platform_played_on = models.CharField(max_length=50)
    game_systems_looking_for = models.CharField(max_length=200)
    campaign_length = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    am_i_a_player = models.BooleanField
    am_i_a_gm = models.BooleanField
    am_i_a_site_manager = models.BooleanField

class FriendsList(models.Model):
    # fk
    user = models.CharField
    friends_list = models.CharField
    friends_status = models.BooleanField

class UserChat(models.Model):
    # fk
    user = models.ForeignKey
    chat = models.ForeignKey

class Chat(models.Model):
    # fk
    user = models.CharField
    chat_history = models.CharField
    field = models.CharField

class Character_Cards (models.Model):
    # fk
    user = models.CharField(max_length=15)
    character_name= models.CharField(max_length=30)
    CharacterDescription = models.CharField(max_length=500)
    CharacterImage = models.ImageField

def __str__(self):
    return self.name


    

    

