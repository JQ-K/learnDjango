#coding:utf-8
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse 
import os
from django.conf import settings
from models import * #导入数据库
from django.core.paginator import *
from django.views.decorators.cache import cache_page #导入缓存包
from django.core.cache import cache
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
def hero_list(request, pindex):#向视图传递参数需要用到url正则表达式
    if pindex  is None:
        pindex = '1' 
    list = HeroInfo.objects.all()
    paginator = Paginator(list,5)
    page = paginator.page(int(pindex))
    print (page.number)
    context = {'page':page}
    return render(request,'herolist.html',context)
    

#省市区选择
def area(request):
    areas = Areas.objects.all()
    context = {'areas':areas}
    return render(request,'area.html',context)

def pro(request):
    data = Areas.objects.filter(parea__isnull=True).values('id','title')
    data = list(data)
    print(data)
    return JsonResponse({'data':data},safe=False)


def city(request,id):
    data = Areas.objects.filter(parea_id=id).values('id','title')
    data = list(data)
    print(data)
    return JsonResponse({'data':data},safe=False)

#自定义编辑器
def html_editor(request):
    return render(request,'html_editor.html')

def content(request):
    html = request.POST.get('hcontent')
    #test1=Test1.objects.get(pk=1) # 更新数据库内容
    #test1.content = html
    #test1.save()
    test1 = Test1()#向数据库中保存数据
    test1.content = html
    test1.save()

    context = {'content': html}
    return render(request, 'htmlshow.html',context)


#缓存
#@cache_page(60*10)
def cache1(request):
    #return HttpResponse('hello')
    #return HttpResponse('helloi2')
    #cache.set('key1','value1',600)#缓存数据
    #print(cache.get('key1'))
    #return render(request, 'cache1.html')

    cache.clear()
    return HttpResponse('ok cache is clear')

