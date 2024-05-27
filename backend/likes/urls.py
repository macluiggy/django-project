from django.urls import path, re_path
from . import views

urlpatterns = [
    path('add/<int:pk>', views.add_like, name='add_like'),
    path('remove/<int:pk>', views.remove_like, name='remove_like'),
]