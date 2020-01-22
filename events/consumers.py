from asgiref.sync import async_to_sync
from django.contrib.auth.models import AnonymousUser
from channels.generic.websocket import JsonWebsocketConsumer
import json

from message.serializers import MessageSerializer

class EventConsumer(JsonWebsocketConsumer):
    def connect(self):
        self.user = self.scope['user']
        if self.user is AnonymousUser:
            self.close()

        self.user_group_name = 'user_%s' % self.user.id

        # Join user group (a group is required to ease the search while sending a message)
        # User groups contain SINGLE channel
        async_to_sync(self.channel_layer.group_add)(
            self.user_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave user group
        async_to_sync(self.channel_layer.group_discard)(
            self.user_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive_json(self, content):                   # receive is useless for now
        print('Attempt to send a message via web-socket detected!')

    def event_notify(self, event):
        event_json = {
            'event_type':   event.json_type,
            'event':        event.json_repr,
        }
        self.send_json(event_json)


    # TODO: add json_type and json_repr to models

