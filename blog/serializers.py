from rest_framework import serializers
from users.serializer import UserSerializer
from .models import Blog, Category
from taggit.serializers import (TagListSerializerField, TaggitSerializer)
from taggit.models import Tag


class CategorySerializer(serializers.ModelSerializer):
    """分类的序列化器"""
    url = serializers.HyperlinkedIdentityField(view_name="category-detail", )

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['created_time']


class BlogSerializer(TaggitSerializer, serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="blog-detail",
                                               lookup_field="slug")
    slug = serializers.SlugField(read_only=True)
    author = serializers.StringRelatedField()
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True,
                                           allow_null=True,
                                           required=False)

    tags = TagListSerializerField()

    def validate_category_id(self, value):
        if not Category.objects.filter(
                id=value).exists() and value is not None:
            raise serializers.ValidationError("分类不存在, 请先创建")
        if value == 0 or not isinstance(value, int):
            raise serializers.ValidationError("请选择一个分类")
        return value

    class Meta:
        model = Blog
        fields = [
            "id",
            "url",
            "slug",
            "title",
            "summery",
            "author",
            "content",
            "tags",
            "category",
            "category_id",
            "created_time",
            "last_updated_time",
        ]


class BlogCategoryDetailSerializer(serializers.ModelSerializer):
    """給文章詳情的嵌套序列化器"""
    url = serializers.HyperlinkedIdentityField(view_name="blog-detail",
                                               lookup_field="slug")

    class Meta:
        model = Blog
        fields = [
            "id",
            "url",
            "slug",
            "title",
            "summery",
            "author",
            "content",
            "category",
            "category_id",
            "created_time",
            "last_updated_time",
        ]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        # 序列化author的详细信息，否则只会序列化出id
        rep['author'] = UserSerializer(instance.author).data
        return rep


class CategoryDetailSerializer(serializers.ModelSerializer):
    """分类详情"""
    articles = BlogCategoryDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'created_time',
            'articles',
        ]


class BlogRecentSerializer(serializers.ModelSerializer):
    """最近发布"""
    url = serializers.HyperlinkedIdentityField(view_name="blog-detail",
                                               lookup_field="slug")
    slug = serializers.SlugField(read_only=True)
    author = serializers.StringRelatedField()
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Blog
        fields = [
            "url",
            "slug",
            "title",
            "author",
            "category",
            "last_updated_time",
        ]


class BlogArchiveSerializer(serializers.ModelSerializer):
    """归档博文"""
    url = serializers.HyperlinkedIdentityField(view_name="blog-detail",
                                               lookup_field="slug")
    slug = serializers.SlugField(read_only=True)
    author = serializers.StringRelatedField()

    class Meta:
        model = Blog
        fields = [
            "url",
            "title",
            "slug",
            "summery",
            "author",
            "created_time",
        ]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        # 序列化author的详细信息，否则只会序列化出id
        rep['author'] = UserSerializer(instance.author).data
        return rep


class TagsSerializer(serializers.ModelSerializer):
    """标签"""
    class Meta:
        model = Tag
        fields = "__all__"
