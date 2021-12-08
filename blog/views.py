from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from .models import Blog, Category
from .serializers import BlogSerializer, CategorySerializer,\
    CategoryDetailSerializer, BlogRecentSerializer, \
    BlogArchiveSerializer, TagsSerializer,BlogListSerializer, \
    BlogSimilarSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication,\
    SessionAuthentication
from .permissions import IsAuthor
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
from rest_framework.serializers import DateField
from rest_framework import status
from rest_framework.response import Response
from taggit.models import Tag
from .pagination import CustomPageNumber
# Create your views here.


class BlogViewSet(viewsets.ModelViewSet):
    """博文視圖集"""
    queryset = Blog.objects.all().order_by('-created_time')
    lookup_field = 'slug'
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated, IsAuthor]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category']
    ordering = ('-created_time')

    @action(methods=['GET'],
            detail=False,
            url_path="archive/dates",
            url_name="archive-date")
    def list_archive_dates(self, request, *args, **kwargs):
        """返回博客的归档日期"""
        dates = Blog.objects.dates("created_time", "month", order="DESC")
        date_field = DateField()
        data = [date_field.to_representation(date) for date in dates]
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['GET'],
            detail=False,
            url_path="archive/tags",
            url_name="archive-tags")
    def list_archive_tags(self, request, *args, **kwargs):
        """返回给定标签名的博文列表/ 分页"""
        tag_name = self.request.query_params.get("tag_name")
        instance = Blog.objects.filter(tags__name__in=[tag_name])
        # serializer = self.get_serializer(instance, many=True)
        serializer = BlogSimilarSerializer(instance,
                                           many=True,
                                           context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if 'prev' in request.query_params:
            instance = Blog.objects.filter(
                created_time__gt=instance.created_time).last()
            if instance is None:
                return Response({"message": "没有上一篇了"})
        elif 'next' in request.query_params:
            instance = Blog.objects.filter(
                created_time__lt=instance.created_time).first()
            if instance is None:
                return Response({"message": "没有下一篇了"})
        elif 'similar' in request.query_params:
            # 根据django-taggit获取相似文章
            instance.similar_posts = instance.tags.similar_objects()
            serializer = self.get_serializer(instance.similar_posts[:3],
                                             many=True)
            return Response(serializer.data)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == "list":
            return BlogListSerializer
        elif self.action == "retrieve" and 'similar' in self.request.query_params:
            return BlogSimilarSerializer
        else:
            return BlogSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    """分类视图集"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def retrieve(self, request, *args, **kwargs):
        # do your customization here
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == "list":
            return CategorySerializer
        else:
            return CategoryDetailSerializer


"""
class TestViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Test.objects.all().order_by('-created_at')
    serializer_class = TestSerializer

    @list_route(methods=['get'], url_path='get-records/(?P<pk>[^/]+)')
    def get_record(self, request, pk):
        self.pagination_class = CustomPageNumber
        queryset = self.filter_queryset(self.queryset.filter(course=pk))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data) 
"""


class BlogRecentView(ListAPIView):
    queryset = Blog.objects.order_by('-last_updated_time')[:3]
    permission_classes = [IsAuthenticated]
    serializer_class = BlogRecentSerializer
    pagination_class = None


class BlogArchiveView(ListAPIView):
    """归档博文视图集"""
    serializer_class = BlogArchiveSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        year = self.kwargs['year']
        month = self.kwargs['month']
        queryset = Blog.objects.filter(
            created_time__year=year,
            created_time__month=month).order_by('-created_time')
        return queryset


class TagViewSet(viewsets.ModelViewSet):
    """标签视图集"""
    serializer_class = TagsSerializer
    pagination_class = None
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Tag.objects.all()
        return queryset