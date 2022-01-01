import json
import time
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
#from users.models import userModel
from .models import Message


class chatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs'].get(
            'room_name', '0')
        self.room_group_name = f'chat_{self.room_name}'
        # join room group
        await self.channel_layer.group_add(self.room_group_name,
                                           self.channel_name)

        await self.accept()

    async def disconnect(self, close_mode):
        # leave room group
        await self.channel_layer.group_discard(self.room_group_name,
                                               self.channel_name)

    async def receive(self, text_data):
        """receive message from websocket"""
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        await self.save_message(self.room_name, message)
        # send message to the group
        await self.channel_layer.group_send(
            self.room_group_name, {
                'type': 'chat_message',
                'message': message,
                'sender': self.scope['user'].username,
            })

    async def chat_message(self, event):
        """receive messsage from room group"""
        message = event['message']
        sender = event['sender']
        # send message to websocket
        await self.send(text_data=json.dumps(
            {
                'message': message,
                'sender': sender,
                'sendtime': time.strftime('%Y-%m-%d %H:%M:%S',
                                          time.localtime()),
            }))

    @sync_to_async
    def save_message(self, room, content):
        user = self.scope['user']

        Message.objects.create(sender=user.username,
                               room=room,
                               message=content)
