# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#富文本编辑器
from tinymce.models import HTML_Field

# Create your models here.
class TypeInfo(models.Modes):
	""" 商品分类"""
	ttitle = models.CharField(max_length=20)
	isDelete = models.BooleanField(default=False)

class GoodsInfo(models.Model):
	"""上商品信息"""
	gtitle = models.CharField(max_length=20)
	# 文件上传需要在settings 设置MEDIA_ROOT
	gpic = models.ImageField(upload_to='df_goods')
	gprice = models.DecimalField(max_digits=5, decimal_places=2)
    isDelete = models.BooleanField(default=False)
    gunit = models.CharField(max_length=20,default="500g")
    gclick = models.IntegerField()
    gjianjie = models.CharField(max_length=200)
    gkucun = models.IntegerField()
    gcontent = HTML_Field()
    gtype = models.ForeignKey(TypeInfo)#外键,商品和分类是一对多关系

