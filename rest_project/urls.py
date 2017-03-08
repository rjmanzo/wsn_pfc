from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/',include(admin.site.urls), name='admin'),
    url(r'^wsn/login/$', views.login, name='login'),
    url(r'^wsn/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'',include('wsn.urls',namespace='wsn'))
]
