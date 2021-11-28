from rest_framework import viewsets
from .serializers import BlogSerializer
from .models import Blog
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication,\
    SessionAuthentication
from .permissions import IsAuthor
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# Create your views here.


class BlogViewSet(viewsets.ModelViewSet):

    queryset = Blog.objects.all().order_by('-created_time')
    lookup_field = 'slug'
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated, IsAuthor]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'slug']
    ordering = ('-created_time')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


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
