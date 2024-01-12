from django.shortcuts import render
from django.contrib.auth.models import User
from .models import ChatRoom, Message


def chat_list(request):
    chat_rooms = ChatRoom.objects.filter(participants=request.user)
    context = {'chat_rooms': chat_rooms}
    
    return render(request, "chat/chat_list.html", context)


def chat(request, username:str):
    """
    username: Is other user's username
    """
    chat_user = User.objects.get(username=username)
    room_name = "room_" + str(min(chat_user.id, request.user.id)) \
        + "_" + str(max(chat_user.id, request.user.id))
    
    chat_room, created = ChatRoom.objects.get_or_create(room_name=room_name)
    chat_room.participants.add(request.user)
    
    messages = Message.objects.filter(
        room=chat_room).order_by('timestamp')

    context={"room_name": room_name,
            "chat_user": chat_user,
            "history_messages": messages}

    return render(request, "chat/chat.html", context)
