# users/serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'is_tutor', 'date_joined', 
                'phone_number', 'name', 'surname', 'address', 'photo']
        read_only_fields = ['date_joined', 'is_tutor']
        extra_kwargs = {'password': {'write_only': True}, 
                        'email':    {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

