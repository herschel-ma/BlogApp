from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView
from django.conf import settings
import requests
from django.shortcuts import redirect
from .models import Profile
from users.models import userModel
from django.contrib import auth
from rest_framework.authtoken.models import Token
# Create your views here.


class githubCreditialView(APIView):
    code = ''
    access_token = ''

    def login_direct(self, request, user):
        setattr(user, 'backend', 'django.contrib.auth.backends.ModelBackend')
        auth.login(request, user)

    # handle github callback to get code received
    def get(self, request):
        self.code = request.GET['code']
        # get access_token
        if not self.code:
            return Response('回调错误，登陆失败', status=status.HTTP_400_BAD_REQUEST)
        try:
            url = 'https://github.com/login/oauth/access_token'
            params = {
                'client_id': settings.GITHUB_CLIENT_ID,
                'client_secret': settings.GITHUB_CLIENT_SECRET,
                'code': self.code,
            }
            headers = {
                "Accept": "application/json"}
            data = requests.post(url, data=params, headers=headers).json()
            if 'error' in data:
                return Response('回调错误，登陆失败',
                                status=status.HTTP_400_BAD_REQUEST)
            self.access_token = data['access_token']
        except Exception as e:
            raise e

        headers = {
            "Authorization": "token "+self.access_token,
            "Accept": "application/json"}

        # get user info
        try:
            data = requests.get('https://api.github.com/user',
                                headers=headers).json()

            if 'error' in data:
                return Response('回调错误，登陆失败',
                                status=status.HTTP_400_BAD_REQUEST)

            # 得到用户的node_id
            node_id = data['node_id']
            # 判断node_id用户是否存在
            if not Profile.objects.filter(github_node_id=node_id).exists():
                user = userModel(username=data['login'],
                                 password=node_id)
                user.save()
                # 创建对应的node_id记录
                add_profile = Profile(user=user,
                                      github_node_id=node_id,
                                      avatar_url=data['avatar_url'],
                                      nickname=data['login']
                                      )
                add_profile.save()
            else:
                # node_id 用户存在， 更新数据
                user = Profile.objects.get(github_node_id=node_id)
                user.avatar_url = data['avatar_url']
                user.save()
            user = userModel.objects.get(username=data['login'])
            self.login_direct(request, user)
            user_token = Token.objects.get(user=user)
            rep = redirect('/')
            rep.set_cookie("token", user_token)
            # return Response(data, status=status.HTTP_200_OK)
            return rep

        except Exception as e:
            raise e
