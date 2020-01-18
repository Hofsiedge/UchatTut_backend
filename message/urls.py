# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.message, name='msg1'),
    path('<int:id>/', views.message, name='msg2'),
]
