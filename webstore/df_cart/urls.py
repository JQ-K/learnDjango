#coding:utf-8
from django.conf.urls import url 
import views


urlpatterns  = [
   url(r'^$',views.cart),
   #第一个数字表示商品id 第二个表示商品数量
   url(r'^add(\d+)_(\d+)/$', views.add),
]