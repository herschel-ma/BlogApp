from django.urls import path
from .views import ListUsersView

urlpatterns = [
    path('user/', ListUsersView.as_view(), name="user"),
]
