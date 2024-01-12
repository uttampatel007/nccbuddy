import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import ChatRoom, Message
from django.contrib.auth.models import User


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        # Get or create the chat room
        chat_room, created = ChatRoom.objects.get_or_create(room_name=self.room_name)
        # Add the current user to the participants list
        if self.scope["user"].is_authenticated:
            chat_room.participants.add(self.scope["user"])

        self.accept()

    # Receive message from WebSocket
    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message_text = text_data_json['message']
        username = text_data_json['username']
        recipient = text_data_json['recipient']
        is_group = text_data_json['is_group']
        
        room_name = self.room_name
        # Retrieve or create the chat room
        chat_room, created = ChatRoom.objects.get_or_create(room_name=room_name)
        sender_user = User.objects.get(username=username)
        
        # Create a new message and save it to the database
        message = Message.objects.create(
            room=chat_room,
            sender=sender_user,
            message=message_text,
            is_group_message=is_group,
        )

        if is_group:
            recipient = chat_room.participants.exclude(username=username)
            chat_room.participants.add(*recipient)
            message.recipient.add(*recipient)
        else:
            recipient = User.objects.get(username=recipient)
            chat_room.participants.add(recipient)
            message.recipient.add(recipient)
        
        # Broadcast the message to other users in the room (as you're already doing)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, 
            {"type": "chat.message", "message": message_text, 
            "username": username, 
            "sender_user_image": sender_user.profile.image_thumbnail_user.url,
            "timestamp": message.timestamp
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]
        username = event["username"]
        sender_user_image = event["sender_user_image"]
        timestamp = event["timestamp"]
        # Send message to WebSocket
        self.send(text_data=json.dumps(
            {"type": "chat", "message": message, "username":username, 
             "sender_user_image":sender_user_image, "timestamp": timestamp.strftime('%b. %d, %Y, %I:%M %p')}
        ))
