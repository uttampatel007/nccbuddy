from django.contrib import admin
from .models import Post, Comment,PostReport,Notification

# Registers blog app the django admin backend.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostReport)
admin.site.register(Notification)

