from rest_framework import serializers
from .models import userModel
from backend_res.models import Profile


class GithubUserInfoSeGithubUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('avatar_url',)


class UserSerializer(serializers.ModelSerializer):
    user = GithubUserInfoSeGithubUserInfoSerializer()

    class Meta:
        model = userModel
        fields = ('username', 'user')
