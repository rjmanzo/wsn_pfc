from django.conf.urls import include, url
from . import views
"""Necesario agregar el nombre de la app para el uso de URL namespace"""

app_name = 'wsn'

urlpatterns = [
    url(r'^$', views.main_page, name='starter'),
    url(r'^wsn/lab-test/$', views.lab_page, name='lab'),
    url(r'^wsn/campo-test-uno/$', views.campo_uno_page, name='campo_uno'),
    url(r'^wsn/campo-test-dos/$', views.campo_dos_page, name='campo_dos'),
    url(r'^api-reg/$', views.DatoList.as_view(), name='api_reg'),
    url(r'^api-config/$', views.ConfiguracionList.as_view(), name='api_config'),
    url(r'^api-graph-lab/$', views.DatosGraphLabList.as_view(), name='api_graph_lab'),
    url(r'^api-table-lab/$', views.DatosTableLabList.as_view(), name='api_table_lab'),
    
]
