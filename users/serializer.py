from rest_framework import serializers
from .models import userModel
from backend_res.models import Profile


class GithubUserInfoSeGithubUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('avatar_url', )


# class postNumerSerializer(serializers.Serializer):
#     Users = userModel.objects.all()
#     post_counts = serializers.IntegerField()
#     for u in Users:
#         post_count = u.articles.all().count()
#         post_counts.append(post_count)


class UserSerializer(serializers.ModelSerializer):
    user = GithubUserInfoSeGithubUserInfoSerializer()
    post_count = serializers.SerializerMethodField("get_user_count")

    def get_user_count(self, obj):
        return obj.articles.count()

    class Meta:
        model = userModel
        fields = ('username', 'user', "post_count")
