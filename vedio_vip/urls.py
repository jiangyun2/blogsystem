#!/usr/bin/python
# -*- coding: utf-8 -*
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view())
]

