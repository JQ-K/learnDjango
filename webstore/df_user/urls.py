#!/usr/bin/env python
# coding=utf-8

from django.conf.urls import url
import views 
urlpatterns=[
       
    url(r'^register$',views.register),
    url(r'^register_handle/$',views.register_handle),
]
