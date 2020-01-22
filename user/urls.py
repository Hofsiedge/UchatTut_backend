# user/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('<int:user_id>', views.single_user, name='single_user'),
    path('profile', views.profile, name='profile')
]
