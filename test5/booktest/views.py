#coding:utf-8
from django.shortcuts import render

from django.http import HttpResponse
import os
from django.conf import settings
from models import * #导入数据库
from django.core.paginator import *
# Create your views here.


def index(request):
    return render(request,'index.html')

# 测试自定义中间件
def MyExp(request):
    a1 = int('abc')
    return HttpResponse('Hello')

#上传文件
def upload_pic(request):
    return render(request,'upload_pic.html')

def upload_handle(request):
    pic1 = request.FILES["pic1"]
    pic_name = os.path.join(settings.MEDIA_ROOT,pic1.name)
    with open(pic_name,'w') as f:
        for i in pic1.chunks():
            f.write(i)
    
    return HttpResponse('<img src="/static/media/{}">'.format(pic1.name))

#进行分页练习
def hero_list(request):
    list = HeroInfo.objects.all()
    for i in list:
        print(i.hname)
    paginator = Paginator(list,5)
    page = paginator.page(1)
    context = {'page':page}
    return render(request,'herolist.html',context)
    

