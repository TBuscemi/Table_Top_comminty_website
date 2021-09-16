from django.db import models


class Chat(models.Model):
    chat_history = models.TextField
    chat_name = models.CharField(max_length=255)
