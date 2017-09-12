from django.conf.urls import include, url
from . import views
"""Necesario agregar el nombre de la app para el uso de URL namespace"""

app_name = 'wsn'

urlpatterns = [
    #index
    url(r'^$', views.main_page, name='starter'),
    #lab
    url(r'^wsn/lab-test/$', views.lab_page, name='lab'),
    url(r'^wsn/lab-test/1/$', views.lab_uno_page, name='lab_uno'),
    url(r'^wsn/lab-test/2/$', views.lab_dos_page, name='lab_dos'),
    #campo
    url(r'^wsn/campo-test/$', views.campo_page, name='campo'),
    url(r'^wsn/campo-test/1/$', views.campo_uno_page, name='campo_uno'),
    url(r'^wsn/campo-test/2/$', views.campo_dos_page, name='campo_dos'),
    #yatchclub
    url(r'^ycsf/$', views.yachtclub_page, name='yachtclub'),
    #Rest configuration
    url(r'^api-reg/$', views.DatoList.as_view(), name='api_reg'),
    url(r'^api-config/$', views.ConfiguracionList.as_view(), name='api_config'),
    #Rest lab
    url(r'^api-graph-lab/1/$', views.DatosGraphLab_Uno_List.as_view(), name='api_graph_lab_uno'),
    url(r'^api-table-lab/1/$', views.DatosTableLab_Uno_List.as_view(), name='api_table_lab_uno'),
    #url(r'^api-graph-lab/2/$', views.DatosGraphLab_Dos_List.as_view(), name='api_graph_lab_dos'),
    #url(r'^api-table-lab/2/$', views.DatosTableLab_Dos_List.as_view(), name='api_table_lab_dos'),
    #Rest campo
    url(r'^api-graph-campo/1/$', views.DatosGraphCampo_Uno_List.as_view(), name='api_graph_campo_uno'),
    url(r'^api-table-campo/1/$', views.DatosTableCampo_Uno_List.as_view(), name='api_table_campo_uno'),
    #url(r'^api-graph-campo/2/$', views.DatosGraphCampo_Dos_List.as_view(), name='api_graph_campo_dos'),
    #url(r'^api-table-campo/2/$', views.DatosTableCampo_Dos_List.as_view(), name='api_table_campo_dos'),
    url(r'^api-graph-yachtclub/1/$', views.DatosGraphYachtclub_List.as_view(), name='api_graph_yachtclub'),
    url(r'^api-table-yachtclub/1/$', views.DatosTableYachtclub_List.as_view(), name='api_table_yachtclub'),
]
