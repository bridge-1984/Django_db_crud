# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, re_path
from apps.home import views

urlpatterns = [
    # The home page
    path('', views.index, name='home'),
    path('tables', views.show, name="show"),
    
    
    # re_path('stu/add/$', views.add_stu),
    # re_path('stu/(\d+)/delete', views.delete_stu),
    # re_path('stu/(\d+)/change', views.change_stu),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
