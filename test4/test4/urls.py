from django.conf.urls import include, url
from django.contrib import admin
from booktest import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'test4.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('booktest.urls', namespace='booktest')),
    #url(r'^$', views.index),
]
