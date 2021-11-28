from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet

router = DefaultRouter()
router.register("blog", BlogViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
