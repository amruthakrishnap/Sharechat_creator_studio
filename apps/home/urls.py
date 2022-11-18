# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
# from .views import Create_NewPost

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('NewPost', views.Create_NewPost, name="NewPost"),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),


]
