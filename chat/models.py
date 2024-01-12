from django.db import models
from django.contrib.auth.models import User


class ChatRoom(models.Model):
    room_name = models.CharField(max_length=100, unique=True)
    participants = models.ManyToManyField(User)


class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    is_group_message = models.BooleanField(default=True)
    recipient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipient', 
        blank=True, null=True)

