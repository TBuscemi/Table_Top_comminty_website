from django.db import models
from django.contrib.auth.modles import User

class Character_Cards (models.Model):
    # fk
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    character_name= models.CharField(max_length=30)
    CharacterDescription = models.CharField(max_length=500)
    CharacterImage = models.ImageField