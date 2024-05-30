from django.urls import path, re_path
from . import views

urlpatterns = [
    # path('add/<int:post_id>', views.add_comment, name='add_like'),
    # path('remove/<int:post_id>', views.remove_comment, name='remove_like'),
    path('create', views.create_permission, name='add_permission'),
    path('get_all', views.list_permission, name='list_permission'),
    path('role_permission/create', views.create_role_permission, name='add_role_permission'),
]