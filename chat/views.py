from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import ChatRoom, Message


def chat_list(request):

    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        participants_usernames = request.POST.getlist('participants')

        # Create a new ChatRoom with the provided data
        chat_room = ChatRoom.objects.create(
            room_name="group_"+str(ChatRoom.objects.count() + 1),  # Assuming you want a unique room_name
            is_group_chat=True,
            group_name=group_name
        )

        # Add the creator (request.user) to the participants
        chat_room.participants.add(request.user)

        # Add the selected participants to the group
        participants = User.objects.filter(username__in=participants_usernames)
        chat_room.participants.add(*participants)

        # Redirect to the chat list page after successful creation
        return redirect('chat:chat_list')

    chat_rooms = ChatRoom.objects.filter(participants=request.user)
    all_participants = request.user.profile.followers.all()

    context = {'chat_rooms': chat_rooms, 'all_participants': all_participants}
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


def group_chat(request, room_name):
    """
    room_name: Room name for the group chat
    """
    try:
        chat_room = ChatRoom.objects.get(room_name=room_name, is_group_chat=True)
    except ChatRoom.DoesNotExist:
        # Handle the case where the group chat room doesn't exist
        # You can redirect the user to an error page or any other appropriate action
        return render(request, "chat/group_chat_not_found.html")

    participants = chat_room.participants.values_list('id', flat=True)
    messages = Message.objects.filter(room=chat_room).order_by('timestamp')

    context = {
        "room_name": room_name,
        "participants": participants,
        "history_messages": messages,
        "chat_room": chat_room
    }

    return render(request, "chat/group_chat.html", context)