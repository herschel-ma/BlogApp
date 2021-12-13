from django.urls import path, include
from .views import ListUserView, ListUsersView, AvatarViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('avatar', AvatarViewSet)
#router.register("user", ListUserView, basename="user")
urlpatterns = [
    path("", include(router.urls)),
    path('user/', ListUserView.as_view(), name="user"),
    path('users/', ListUsersView.as_view(), name="users"),
]
