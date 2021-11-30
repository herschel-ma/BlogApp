from rest_framework import serializers
from .models import Blog, Category


class CategorySerializer(serializers.ModelSerializer):
    """分类的序列化器"""
    url = serializers.HyperlinkedIdentityField(view_name="category-detail", )

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['created_time']


class BlogSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="blog-detail",
                                               lookup_field="slug")
    slug = serializers.SlugField(read_only=True)
    author = serializers.StringRelatedField()
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True,
                                           allow_null=True,
                                           required=False)

    def validate_category_id(self, value):
        if not Category.objects.filter(
                id=value).exists() and value is not None:
            raise serializers.ValidationError(
                "Category with id {} not exists.".format(value))
        return value

    class Meta:
        model = Blog
        fields = [
            "id",
            "url",
            "slug",
            "title",
            "author",
            "content",
            "category",
            "category_id",
            "created_time",
            "last_updated_time",
        ]


class BlogDetailSerializer(BlogSerializer):
    pass


class BlogCategoryDetailSerializer(serializers.ModelSerializer):
    """給文章詳情的嵌套序列化器"""
    url = serializers.HyperlinkedIdentityField(view_name="blog-detail",
                                               lookup_field="slug")

    class Meta:
        model = Blog
        fields = [
            'url',
            'title',
        ]


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