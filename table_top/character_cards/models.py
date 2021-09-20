from django.db import models
from django.contrib.auth.models import User

class CharacterCards (models.Model):
    # fk
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    character_name= models.CharField(max_length=30)
    character_description = models.CharField(max_length=500)
    character_image = models.ImageField()