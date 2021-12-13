from rest_framework import serializers
from .models import userModel, Avatar
from backend_res.models import Profile


class GithubUserInfoSeGithubUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('avatar_url', )


class AvatarSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='avatar-detail')

    class Meta:
        model = Avatar
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    user = GithubUserInfoSeGithubUserInfoSerializer(read_only=True)
    post_count = serializers.SerializerMethodField("get_user_count")
    # 图片字段
    avatar = AvatarSerializer(read_only=True)
    avatar_id = serializers.IntegerField(write_only=True,
                                         allow_null=True,
                                         required=False)

    username = serializers.CharField(read_only=True)

    def get_user_count(self, obj):
        return obj.articles.count()

    # 验证图片 id 是否存在
    # 不存在则返回验证错误
    def validate_avatar_id(self, value):
        if not Avatar.objects.filter(id=value).exists() and value is not None:
            raise serializers.ValidationError("头像不存在，请重新上传")

        return value

    class Meta:
        model = userModel
        fields = ('id', 'username', 'user', "post_count", "avatar",
                  "description", "avatar_id")
