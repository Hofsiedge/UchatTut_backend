# lesson/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.lessons, name='lessons'),
    path('<int:id>/', views.lesson, name='lesson'),
]
