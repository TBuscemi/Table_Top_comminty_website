from django.db import models
from django.contrib.auth.models import User
from chat.models import Chat


class UserChat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
