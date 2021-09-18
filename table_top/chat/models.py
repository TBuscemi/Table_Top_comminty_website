from django.db import models


class Chat(models.Model):
    chat_history = models.TextField(max_length=60000)
    chat_name = models.CharField(max_length=255)
