# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:chat_id>/', views.chat, name='chat'),
]
