from table_top.chat.models import Chat
from django.db import models
from chat import chat
from django.contrib.auth.modles import User

class UserChat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(chat, on_delete=models.CASCADE)
