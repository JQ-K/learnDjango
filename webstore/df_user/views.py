# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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
        return redirect('/user/register/')
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

        
