from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer, AvatarSerializer
from .models import userModel, Avatar
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework import viewsets

# Create your views here.


class ListUserView(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = None
    serializer_class = UserSerializer

    def get(self, request, format=None):
        serializer = UserSerializer(request.user, context={'request': request})
        return Response(serializer.data)

    def put(self, request, format=None):
        serializer = UserSerializer(data=request.data,
                                    context={'request': request})
        if serializer.is_valid(raise_exception=True):
            user = request.user
            user.avatar_id = request.data.get('avatar_id')
            user.description = request.data.get('description')
            user.save()
            return Response({"detail": "修改成功"})
        return Response({"detail": "数据不合法"})


class ListUsersView(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        Users = userModel.objects.all()
        serializer = UserSerializer(Users,
                                    many=True,
                                    context={'request': request})
        return Response(serializer.data)


class AvatarViewSet(viewsets.ModelViewSet):
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]