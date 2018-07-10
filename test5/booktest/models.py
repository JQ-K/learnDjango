#coding:utf-8
from django.db import models

# Create your models here.

class UserInfo(models.Model):
    uname = models.CharField(max_length = 10)
    upwd = models.CharField(max_length=40)
    isDelete = models.BooleanField(default=False)


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(db_column='pub_date')
    bread=models.IntegerField(default=0)
    bcomment =models.IntegerField(null=False)
    isDelete = models.BooleanField(default=False)



class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=True)
    hcontent = models.TextField()   
    isDelete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo)

class Areas(models.Model):
    title = models.CharField(max_length=10)
    parea = models.ForeignKey('self', null=True, blank=True)#mysql 中外键自关联
    


