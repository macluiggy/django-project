from django.urls import path, re_path
from . import views

urlpatterns = [
    # path('posts/', views.post_list, name='post_list'),
    # re_path(r'^posts/$', views.get_posts, name='post_list'),
    path('', views.get_posts),
]