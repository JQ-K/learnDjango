# coding:utf-8
from django.db import models

# Create your models here

# 生成sql语句和表格，Django中不需要面向数据库写sql语句

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    def __str__(self):
        return self.btitle.encode('utf8')
    
class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    hbook = models.ForeignKey(BookInfo) # 引用外i键
    
    def __str__(self):
        return self.hname.encode('utf8')





