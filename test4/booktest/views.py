#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from models import *
# Create your views here.

def index(request):
    #hero = HeroInfo.objects.get(pk=1)
    #context = {'hero':hero}
    list = HeroInfo.objects.filter(isDelete=False)
    context = {'list': list}
    return render(request,'index.html', context)

def show(request, id, id2):
    context = {'id':id}
    return render(request, 'show.html',context)

# 用于练习模板的继承
def index2(request):
    return render(request, 'index2.html')

def user1(request):
    return render(request, 'user1.html')

def user2(request):
    return render(request, 'user2.html')

# html 转义练习
def html_test(request):
    context ={'t1': '<h1>123</h1>'}
    return render(request, 'html_test.html',context)

# csrf
def csrf1(request):
    return render(request, 'csrf1.html')

def csrf2(request):
    uname = request.POST['uname']
    return HttpResponse(uname)

