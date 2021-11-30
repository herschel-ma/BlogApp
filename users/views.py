from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer
from .models import userModel

# Create your views here.


class ListUserView(APIView):
    def get(self, request, format=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class ListUsersView(APIView):
    def get(self, request, format=None):
        Users = userModel.objects.all()
        serializer = UserSerializer(Users, many=True)
        return Response(serializer.data)