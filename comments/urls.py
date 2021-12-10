from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from comments.views import CommentViewSet
from comments.models import Comment

router = DefaultRouter()
router.register("comments", CommentViewSet, basename="comments")

urlpatterns = [
    path("", include(router.urls)),
]
