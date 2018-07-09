#!/usr/bin/env python
# coding=utf-8

from django.conf.urls import url 
import views

urlpatterns=[

    url(r'^$', views.index),
    url(r'^myexp$', views.MyExp),
    url(r'^uploadPic$', views.upload_pic),

    url(r'^uploadhandle$', views.upload_handle),
    url(r'^herolist/(\d+)*$', views.hero_list),
]
