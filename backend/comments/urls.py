from django.urls import path, re_path
from . import views

urlpatterns = [
    path('add/<int:post_id>', views.add_comment, name='add_like'),
    path('remove/<int:post_id>', views.remove_comment, name='remove_like'),
]