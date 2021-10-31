from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer

# Create your views here.


class ListUsersView(APIView):

    def get(self, request, format=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
