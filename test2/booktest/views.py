# coding:utf-8
from django.shortcuts import render
from models import *
from django.db.models import Max, F, Q

# Create your views here.

def index(request):
    #list = BookInfo.books1.filter(heroinfo__hcontent__contains='六')
    #list = BookInfo.books1.filter(pk__lte=3)
    #Max1 = BookInfo.books1.aggregate(Max('bpub_date')) # 聚合
    #list = BookInfo.books1.filter(bread__gt=F('bcomment'))#两个列比较使用F
    #list = BookInfo.books1.filter(pk__lt=6,btitle__contains='八')# 与的逻辑用法
    list = BookInfo.books1.filter(Q(pk__lt=4)|Q(btitle__contains='1'))# or逻辑使用Q语句
    context = {'list':list
              # 'Max1':Max1
              }
    return render(request, 'index.html',context) 
