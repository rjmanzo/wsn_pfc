from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
#from rest_framework.authtoken import views as authviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/',include(admin.site.urls), name='admin'),
    url(r'^wsn/login/$', views.login, name='login'),
    url(r'^wsn/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    #url(r'^api-token-auth/$', authviews.obtain_auth_token, namespace='api-token-auth'),
    url(r'',include('wsn.urls',namespace='wsn')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
