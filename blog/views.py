from rest_framework import viewsets
from .models import Blog, Category
from .serializers import BlogSerializer, CategorySerializer, CategoryDetailSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication,\
    SessionAuthentication
from .permissions import IsAuthor
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
# Create your views here.


class BlogViewSet(viewsets.ModelViewSet):
    """博文視圖集"""
    queryset = Blog.objects.all().order_by('-created_time')
    lookup_field = 'slug'
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated, IsAuthor]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'slug']
    ordering = ('-created_time')

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
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    """分类视图集"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

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
