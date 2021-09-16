from django.db import models
from django.contrib.auth.modles import User

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat_history = models.TextField
    chat_name = models.CharField
