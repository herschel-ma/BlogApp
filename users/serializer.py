from rest_framework import serializers
from. models import userModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = userModel
        fields = ('username',)
