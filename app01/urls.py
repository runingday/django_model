#!/usr/bin/env python
#coding:utf-8

from django.conf.urls import url, include
# from django.contrib import admin
from app01.views import *

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^login/$', login),
    url(r'^index/$', index),
    url(r'^host/$', host),
    url(r'^register/$', register),

]
