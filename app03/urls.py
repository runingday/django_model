#!/usr/bin/env python
#coding:utf-8

from django.conf.urls import url, include
from app03 import views
# from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index),

]
