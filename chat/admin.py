from django.contrib import admin

from .models import ChatRoom, Message


admin.site.register(ChatRoom)


admin.site.register(Message)
