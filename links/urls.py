from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from .models import Links, Category
from .views import LinksViewSet, LinksCategoryViewSet, LinksThumbnailViewSet

router = DefaultRouter()
router.register("links", LinksViewSet)
router.register("linksCategory", LinksCategoryViewSet)
router.register('linsThumbnailUpload', LinksThumbnailViewSet)

urlpatterns = [
    path("", include(router.urls)),
]