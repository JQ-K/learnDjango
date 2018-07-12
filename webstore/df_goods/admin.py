# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import TypeInfo, GoodsInfo

# Register your models here.


class TypeInfoAdmin(admin.ModelAdmin):
	list_display = ['id','ttitle']

class GoodsInfoAdmin(admin.ModelAdmin):
	list_per_page = 15
	list_display = ['id', 'gtitle', 'gprice', 'gunit', 'gclick', 'gkucun','gcontent', 'gtype']

# 注册到后台
admin.site.register(TypeInfo, TypeInfoAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)

#或者使用装饰器注册
# @admin.register(TypeInfo)
# class TypeInfoAdmin(admin.ModelAdmin):
# 	list_display = ['id','ttile']

# @admin.register(GoodsInfo)
#   class GoodsInfoAdmin(admin.ModelAdmin):
# 	lisr_per_page =15
# 	list_display = ['id', 'gtitle', 'gprice', 'gunit', 'gclick', 'gkucun','gcontent', 'gtype']