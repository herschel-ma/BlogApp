"""BlogApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

# from users.forms import UserForm
# from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name="index"),
    # path('accounts/register/',
    #      RegistrationView.as_view(
    #          form_class=UserForm,
    #          success_url='/'
    #      ), name="register",
    #      ),
    path('accounts/', include('allauth.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),

    path('api/', include('users.urls')),
    path('api/', include('articles.urls')),

    path('auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/', include('backend_res.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]
