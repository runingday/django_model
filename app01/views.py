#encoding:utf-8
from django.shortcuts import render, render_to_response,redirect
from django.template.context_processors import request
from django.http.response import HttpResponse
from models import *
# Create your views here.

def register(request):

    '''
    #创建用户类型
    t1 = UserType.objects.create(name="超级管理员")
    t2 = UserType.objects.create(name="普通管理员")

    #创建用户
    u1 = UserInfo.objects.create(username="alon",
                                 password="123",
                                 email='runingday@126.com',
                                 user_type=t1
                                )
    t3 = UserType.objects.get(name="超级管理员")
    u2 = UserInfo.objects.create(username="alon",
                                 password="123",
                                 email='runingday@126.com',
                                 user_type=t3
                                 )

    t4 = UserType.objects.get(name="普通管理员")
    u3 = UserInfo.objects.create(username="alon",
                                 password="123",
                                 email='runingday@126.com',
                                 user_type=t4
                                 )
    groupObjA = UserGroup.objects.create(GroupName="主机A")
    groupObjA.user.add(u1)
    groupObjB = UserGroup.objects.create(GroupName="主机B")
    groupObjB.user.add(u1)
    '''
    return HttpResponse("注册成功")


def login(request):

    ret = {"status":""}
    if request.method == 'POST':
        username = request.POST.get("username", None)
        password = request.POST.get('password', None)

        is_empty = all([username, password])

        if is_empty:
            count = UserInfo.objects.filter(username=username,password=password).count()

            if count == 1:
                return redirect('/app01/index/')
            else:
                ret['status'] = "用户名和密码错误"
        else:
            ret['status'] = "用户名和密码不能为空"
    return render_to_response('app01/login.html', ret)



    return  render_to_response("app01/login.html", ret)

def index(request):

    return render_to_response("app01/index.html")

def host(request):
    ret = {"status": "", "data": None, "group":None}

    usergroup = UserGroup.objects.all()
    ret['group'] = usergroup

    #新建主机
    if request.method == 'POST':
        hostname = request.POST.get('hostname', None)
        ip = request.POST.get('ip', None)

        groupId = request.POST.get('group', None)

        #验证用户输入是否为空
        is_auth = all([hostname, ip])

        if is_auth:
            groupObj = UserGroup.objects.get(id=groupId)
            Asset.objects.create(hostname=hostname,
                                 ip=ip,
                                 user_group=groupObj
                                 )
        else:
            ret['status'] = 'hostname或ip不能为空'

    data = Asset.objects.all()
    ret['data'] = data


    #obj = Asset.objects.filter(user_group__GroupName="主机B")
    assetList = Asset.objects.filter(user_group__id=2)
    for item in assetList:
        print item
        #print item.hostname
        #print item.ip
        #print item.user_group
        #print item.user_group.GroupName

    #跨表查用两个__,跨表取用.
    #hostall = Asset.objects.filter(user_group__id="2")

    return render_to_response("app01/host.html", ret)

