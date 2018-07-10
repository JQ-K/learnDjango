#coding:utf-8
from django.contrib import admin
from models import *
# Register your models here.

@admin.register(BookInfo)#装饰器方式注册
class BookInfoAdmin(admin.ModelAdmin):
   list_display = ['id','btitle', 'bpub_date'] 

#admin.site.register(BookInfo, BookInfoAdmin) #admin 注册目的是后台管理 数据库

@admin.register(Test1)
class TestAdmin(admin.ModelAdmin):
    list_display = ['id','content']
