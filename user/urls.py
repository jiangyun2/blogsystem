#!/usr/bin/python
# -*- coding: utf-8 -*

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='user_index'),
    path('register', views.UserRegister.as_view(), name='user_register'),
    path('login', views.UserLogin.as_view(), name='user_login'),
    path('updatepassword', views.UserUpdatePassword.as_view(), name='user_updatepassword'),
    path('logout', views.user_logout, name='user_logout'),
]