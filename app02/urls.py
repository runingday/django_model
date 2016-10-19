#!/usr/bin/env python
#coding:utf-8

from django.conf.urls import url, include
from app02 import views
# from django.contrib import admin
from app01.views import *

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^many/$', views.index),

]
