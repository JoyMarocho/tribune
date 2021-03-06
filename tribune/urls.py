"""tribune URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import re_path as url,include
from django.contrib import admin
# from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'', include('news.urls')),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'accounts/', include('django_registration.backends.one_step.urls')),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'logout/', auth_views.LogoutView.as_view(), {"next_page": '/'}),
    url(r'tinymce/', include('tinymce.urls')),
    
]
