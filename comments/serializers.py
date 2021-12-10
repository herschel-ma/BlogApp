from rest_framework import serializers
from comments.models import Comment
from users.serializer import UserSerializer
from blog.models import Blog


class CommentChildrenSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='comments-detail')
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        exclude = [
            'parent',
            'article',
        ]


class CommentSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='comments-detail')
    author = UserSerializer(read_only=True)
    isShow = serializers.BooleanField(read_only=True)
    article = serializers.HyperlinkedRelatedField(
        view_name='blog-detail',
        read_only=True,
        lookup_field='slug',
    )
    article_id = serializers.IntegerField(write_only=True,
                                          allow_null=False,
                                          required=True)
    parent = CommentChildrenSerializer(read_only=True)
    parent_id = serializers.IntegerField(write_only=True,
                                         allow_null=True,
                                         required=False)

    def update(self, instance, validated_data):
        validated_data.pop('parent_id', None)
        return super().update(instance, validated_data)

    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {'created_time': {'read_only': True}}
