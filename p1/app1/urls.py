from django.urls import path
from . import views

urlpatterns = [
    path('encode/', views.encode_message, name='encode/'),
]