#!/usr/bin/env python
# coding=utf-8

from django.conf.urls import url 

import views

urlpatterns =[
    url(r'^$',views.index, name='index'),
    url(r'^(?P<p2>\d+)/(?P<p3>\d+)/(?P<p1>\d+)$', views.detail, name='detail'),
    url(r'^test1/$',views.get_test1),
    url(r'^test2/$',views.get_test2),
    url(r'^test3/$',views.get_test3),
    url(r'^postTest1/$',views.post_test1),
    url(r'^postTest2$',views.post_test2),
    url(r'^cookieTest/$',views.cookie_test),
    url(r'^redTest1/$', views.redirect_test1),
    url(r'^redTest2/$', views.redirect_test2),
    url(r'^session1/$', views.session1),
    url(r'^session2/$', views.session2),
    url(r'^session2_handle$', views.session2_handle),
    url(r'^session3/$', views.session3),
]
