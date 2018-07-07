from django.conf.urls import url 

import views
urlpatterns =[
      url(r'^$', views.index, name='index'),
      url(r'^(\d+)/(\d+)$', views.show, name='show'),
      url(r'^index2$', views.index2,name='index2'),
      url(r'^user1$', views.user1,name='user1'),
      url(r'^user2$', views.user2,name='user2'),
      url(r'^html_test$', views.html_test, name='html_test'),
      url(r'^csrf1$', views.csrf1),
      url(r'^csrf2$', views.csrf2),
      url(r'^verifyCode$', views.verify_code),
      url(r'^verifyTest1$', views.verify_test1),
      url(r'^verifyTest2$', views.verify_test2),
]
