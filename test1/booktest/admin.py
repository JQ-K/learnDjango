# coding:utf8


from django.contrib import admin
from models import *
# Register your models here.

class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    extra =3


class BookInfoAdmin(admin.ModelAdmin):
    """自定义admin管理页面"""
    list_display = ['id', 'btitle', 'bpub_date'] #管理页面显示
    list_filter = ['btitle']
    search_fields = ['btitle']
    fieldsets = [
        ('base', {'fields':['btitle']}),

        ('super', {'fields':['bpub_date']})
         ]

    inlines = (HeroInfoInline,)


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hanme','hbook']

admin.site.register(BookInfo, BookInfoAdmin)

admin.site.register(HeroInfo)
