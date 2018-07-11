# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from models import *
from hashlib import sha1

# Create your views here.

def register(request):
    return render(request,'df_user/register.html')


def register_handle(request):
    # 接收用户输入
    post = request.POST 
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')
    #判断两次密码是否一致
    if upwd != upwd2:
        return HttpResponseRedirect('/user/register/')
    # 密码加密
    s1 = sha1()
    s1.update(upwd)
    upwd3 = s1.hexdigest()
    # 创建对象
    user=UserInfo()
    user.uname = uname
    user.upwd = upwd3#存取的密码是使用sha1加密后的密码
    user.uemail = uemail
    user.save()
    #注册成功转到登录页面
    return HttpResponseRedirect('/user/login/')

#判断注册用户名是否存在，需要配合js完成
def register_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})


#登录
def login(request):
    uname = request.COOKIES.get('uname','')
    context={'title': '用户登录', 'error_name': 0, 'error_pwd':0, 'uname':uname}
    return render(request,'df_user/login.html',context)

def login_handle(request):
    #接收请求的信息
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    jizhu = post.get('jizhu', 0)
    #根据用户名查询对象
    users =UserInfo.objects.filter(uname=uname)#如果没有此用户返回空列表[]
    print(uname)
    #判断：如果未查则用户名错误，如果查到则判断密码是否正确，正确转到用户中心
    if len(users) ==1:
        s1 = sha1()
        s1.update(upwd)
        if s1.hexdigest() == users[0].upwd:
            red = HttpResponseRedirect('/user/info/')
            #记住用户名
            if jizhu !=0:
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname', '',max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return red
        else:
            context = {'title': '用户登录', 'error_name':0, 'error_pwd':1,  'uname':uname,'upwd':upwd}
            return render(request, 'df_user/login.html', context)
    else:
        context = {'title': '用户登录', 'error_name':1, 'error_pwd': 0, 'uname':uname, 'upwd':upwd}
        return render(request, 'df_user/login.html', context)


        
