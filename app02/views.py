#encoding:utf-8
from django.shortcuts import render, render_to_response, HttpResponse, redirect
from app02 import models



# Create your views here.

def index(request):

    u1 = models.UserInfo.objects.get(id=1)
    g1 = models.UserGroup.objects.get(id=1)

    #g1.user.add(u1) #有多对多字段   要查看多对多是在哪个model类里面
    #u1.usergroup_set.add(g1) #无多对多字段




    return HttpResponse()