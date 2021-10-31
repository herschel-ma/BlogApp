from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import GithubLoginView, githubCreditialView

urlpatterns = [
    path('github/', GithubLoginView.as_view(), name="github_login"),
    path('github/callback',
         githubCreditialView.as_view(), name="github_callback"),
    path('github/get_auth_token', obtain_auth_token, name="github_auth_token")
]
