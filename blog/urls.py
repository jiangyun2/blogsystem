#!/usr/bin/python
# -*- coding: utf-8 -*

from django.urls import path
from . import views
# 导入login_required
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    # path('', views.index, name='blog_index'),
    path('add/', permission_required('user.add_blogcontent')(views.AddBlog.as_view()), name='addblog'),
    path('update/<blog_id>/', views.UpdateBlog.as_view(), name='updateblog'),
    path('list/', views.bloglist, name='bloglist'),
    path('delete/<blog_id>/', views.deleteblog, name='deleteblog'),
    path('blog/<blog_id>/', views.detialblog, name='detialblog'),
]
