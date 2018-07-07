# coding:utf-8

from django.db import models

# Create your models here.


class BookInfoManager(models.Manager):
    def get_query(self):
        return super(BookInfoManager, self).get_query().filter(isDelete=False)
    
    # 管理器中使用实例创建对象参见34行推荐使用
    def create(self, btitle, bpub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.bread = 0
        b.bcomment = 0
        b.isDelete = False
        return b
    

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(db_column='pub_date')
    bread=models.IntegerField(default=0)
    bcomment =models.IntegerField(null=False)
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = 'bookinfo'
    books1 = models.Manager()
    books2 = BookInfoManager()

    # 更方便的创建对象，不用 __init__是因为继承的model 使用了__init__新的会替换原来的功能
    @classmethod
    def create(cls,btitle, bpub_date):
        b=BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.bread =0
        b.bcomment =0
        b.isDelete=False
        return b


class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=True)
    hcontent = models.TextField()
    isDelete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo)




    
