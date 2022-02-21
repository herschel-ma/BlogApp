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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView

# from users.forms import UserForm
# from django_registration.backends.one_step.views import RegistrationView
# drf_yasg
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version="v1",
        description="Herschel 的博客api",
        terms_of_service="",
        contact=openapi.Contact(email="maliang_gs@126.com"),
        license=openapi.License(name="GPLv3 License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name="index"),
    path('', include('django.contrib.auth.urls')),
    path('api/', include('users.urls')),
    path('api/', include('blog.urls')),
    path('api/', include('comments.urls')),
    path('api/', include('chat.urls')),
    path('api/', include('links.urls')),
    path('mdeditor/', include('mdeditor.urls')),
    path('auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/', include('backend_res.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path(r"swagger(?P<format>\.json|\.yaml)",
            schema_view.without_ui(cache_timeout=0),
            name="schema-json"),
    path('swagger/',
         schema_view.with_ui("swagger", cache_timeout=0),
         name="schema-swagger-ui"),
    path('redoc/',
         schema_view.with_ui("redoc", cache_timeout=0),
         name="schema-redoc"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
