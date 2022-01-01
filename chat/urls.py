from django.urls import path
from . import views

urlpatterns = [
    path('messages/<int:room_name>/', views.message_list, name="messages")
]
