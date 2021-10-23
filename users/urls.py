from django.urls import path
from .views import ListUsers

urlpatterns = [
    path('user/', ListUsers.as_view(), name="user"),
]
