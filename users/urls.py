from django.urls import path
from .views import ListUserView, ListUsersView

urlpatterns = [
    path('user/', ListUserView.as_view(), name="user"),
    path('users/', ListUsersView.as_view(), name="user"),
]
