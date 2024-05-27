"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path, re_path
from .view import get_all_users, login, register, profile, update_user

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('auth/login', login),
    re_path('auth/register', register),
    re_path('auth/profile', profile),
    re_path('users/get_all', get_all_users),
    path('users/update/<int:pk>', update_user),
    path('posts/', include('posts.urls')),
    path('likes/', include('likes.urls')),
]
