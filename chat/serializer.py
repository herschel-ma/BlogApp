from .models import Message
from rest_framework import serializers
from users.serializer import UserSerializer


class UserProfileSerilizer(UserSerializer):
    # 在线？
    pass


class MessageSerializer(serializers.Serializer):
    sender = serializers.UserProfileSerilizer(many=False)

    class Meta:
        model = Message
        fields = ['sender', 'message', 'created_time']
