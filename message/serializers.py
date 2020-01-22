# message/serializers.py
from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'time', 'text']
        read_only_fields = ['time'] # , 'sender']
    
    def create(self, validated_data):
        message = Message(
            text=validated_data['text'],
            sender=validated_data['sender'],
        )
        message.save()
        return message
