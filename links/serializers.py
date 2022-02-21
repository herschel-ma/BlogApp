from asyncore import read
from cProfile import label
from rest_framework import serializers
from .models import Category, Links, LinksThumbnail


class LinksCategorySerializer(serializers.ModelSerializer):
    """分类的序列化器"""
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['created_time']

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def validate_title(self, value):
        if self.context.get('request').method == 'POST':
            if Links.objects.filter(title=value):
                raise serializers.ValidationError("分类重复")
        return value


class LinksThumbnailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='linksthumbnail-detail')

    class Meta:
        model = LinksThumbnail
        fields = '__all__'


class LinksSerializer(serializers.ModelSerializer):
    """友链序列化器"""
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), label="分类", help_text="分类")
    title = serializers.CharField(max_length=50, label="标题", help_text="标题")
    description = serializers.CharField(label="描述", help_text="描述")
    show = serializers.SerializerMethodField(read_only=True)
    thumbnail_url = serializers.URLField(label="封面", help_text="封面")
    link_url = serializers.URLField(required=True,
                                    label="链接地址",
                                    help_text="链接地址")
    created_time = serializers.DateTimeField(label="添加时间",
                                             help_text="添加时间",
                                             read_only=True)
    last_updated_time = serializers.DateTimeField(read_only=True,
                                                  label="更新时间",
                                                  help_text="更新时间")

    # https://stackoverflow.com/questions/28945327/django-rest-framework-with-choicefield
    # get human readable stuff.
    def get_show(self, obj):
        return obj.get_show_display()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["category"] = instance.category.title
        return representation

    def validate_title(self, value):
        if self.context.get('request').method == 'POST':
            if Links.objects.filter(title=value):
                raise serializers.ValidationError("链接标题重复")
        return value

    class Meta:
        model = Links
        fields = [
            "id",
            "title",
            "description",
            "show",
            "thumbnail_url",
            "link_url",
            "category",
            "created_time",
            "last_updated_time",
        ]
