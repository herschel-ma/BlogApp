from django.shortcuts import render
from .models import Links, Category, LinksThumbnail
from .serializers import LinksSerializer, LinksCategorySerializer, LinksThumbnailSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication,\
    SessionAuthentication


# Create your views here.
class LinksThumbnailViewSet(viewsets.ModelViewSet):
    """封面视图集"""
    queryset = LinksThumbnail.objects.all()
    serializer_class = LinksThumbnailSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = None


class LinksViewSet(viewsets.ModelViewSet):
    """友链视图集"""
    queryset = Links.objects.all()
    serializer_class = LinksSerializer
    filter_backends = [DjangoFilterBackend]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = None
    filterset_fields = [
        'category',
        'show',
    ]
    ordering = ('-created_time')


class LinksCategoryViewSet(viewsets.ModelViewSet):
    """分类视图集"""
    queryset = Category.objects.all()
    serializer_class = LinksCategorySerializer
    filter_backends = [SearchFilter]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = None
    search_fields = [
        'title',
    ]

    ordering = ('-created_time')