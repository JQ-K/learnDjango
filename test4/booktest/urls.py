from django.conf.urls import url 

import views
urlpatterns =[
      url(r'^$', views.index, name='index'),
      url(r'^(\d+)/(\d+)$', views.show, name='show'),
      url(r'^index2$', views.index2,name='index2'),
      url(r'^user1$', views.user1,name='user1'),
      url(r'^user2$', views.user2,name='user2'),
      url(r'^html_test$', views.html_test, name='html_test'),
]
