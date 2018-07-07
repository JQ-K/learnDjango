from django.db import models

# Create your models here.

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(db_column='pub_date')
    bread = models.IntegerField()
    bcomment = models.IntegerField()
    isDelete = models.BooleanField()
    class Meto():
        db_table='bookinfo'

class Hero_info(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.TextField()
    isDelete = models.BooleanField()
    book = models.ForeingKey('BookInfo')

    



