# chat/serializers.py
from rest_framework import serializers
from .models import Chat
from user.models import User


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'users', 'name', 'messages']
        extra_kwargs = {'messages': {'write_only': True}}
    
    def create(self, validated_data):
        chat = Chat(
            name=validated_data['name'],
        )

        """
        for user_id in validated_data['users']:
            user = User.objects.get(id=int(user_id))
            chat.users.add(user)
        """
        chat.save()
        for user in validated_data['users']:
            chat.users.add(user)

        return chat
