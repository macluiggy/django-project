from django.urls import path, re_path
from . import views

urlpatterns = [
    # path('posts/', views.post_list, name='post_list'),
    # re_path(r'^posts/$', views.get_posts, name='post_list'),
    path('get_all', views.get_posts),
    path('create', views.create_post),
]