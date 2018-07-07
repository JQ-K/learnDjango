#coding:utf-8
from django.shortcuts import render
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
