from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from blog.models import Blog
from .views import BlogViewSet, CategoryViewSet, BlogRecentView, BlogArchiveView

router = DefaultRouter()
router.register("blog", BlogViewSet)
router.register("category", CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("blog_recent", BlogRecentView.as_view(), name="blog_recent"),
    re_path(r'^blog/archive/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$',
            BlogArchiveView.as_view())
]
