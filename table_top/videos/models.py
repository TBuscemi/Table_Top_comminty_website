from django.db import models

# Create your models here.

class Videos(models.Model):
    dungeon_and_dragons= models.CharField(max_length=150)
    pathfinder= models.CharField(max_length=150)
    roll20= models.CharField(max_length=150)
    fantasy_grounds= models.CharField(max_length=150) 
