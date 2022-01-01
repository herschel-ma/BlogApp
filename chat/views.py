from django.shortcuts import render
from .models import Message
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def message_list(request, room_name=None):
    messages = Message.objects.filter(room=room_name).values(
        "message", "sender", "created_time")[:10]
    return JsonResponse(list(messages), safe=False)
