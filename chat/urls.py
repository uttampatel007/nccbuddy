from django.urls import path
from . import views

app_name = "chat"

urlpatterns = [
    path('', views.chat_list, name='chat_list'),
    path('<str:username>/', views.chat, name='chat'),
    path('group/<str:room_name>/', views.group_chat, name='group_chat'),
]

