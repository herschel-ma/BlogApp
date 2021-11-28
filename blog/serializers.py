from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    author = serializers.StringRelatedField()

    class Meta:
        model = Blog
        fields = "__all__"
