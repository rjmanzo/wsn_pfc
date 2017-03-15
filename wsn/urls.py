from django.conf.urls import include, url
from . import views
"""Necesario agregar el nombre de la app para el uso de URL namespace"""

app_name = 'wsn'

urlpatterns = [
    url(
        regex='^$',
        view= views.main_page,
        name= 'starter'
    ),
    url(
        regex='^wsn/lab-test/$',
        view= views.lab_page,
        name= 'lab'
    ),
    url(
        regex='^wsn/campo-test-uno/$',
        view= views.campo_uno_page,
        name= 'campo_uno'
    ),
    url(
        regex='^wsn/campo-test-dos/$',
        view= views.campo_dos_page,
        name= 'campo_dos'
    ),
    url(
        regex='^api-reg/$',
        view= views.DatoList.as_view(),
        name= 'api_reg'
    ),
    url(
        regex='^api-config/$',
        view= views.ConfiguracionList.as_view(),
        name= 'api_config'
    ),
    url(
        regex='^api-graph-lab/$',
        view= views.DatosTablaLabList.as_view(),
        name= 'api_graph_lab'
    ),
    url(
        regex='^api-table-lab/$',
        view = views.TablaLabsListJson.as_view(),
        name='tabla_lab_list_json'
    ),
    #url(r'^locaciones.json$', views.LocacionesLayer.as_view(properties=('locacion_descrip','wsn_descrip')), name='locaciones_nodos'),
]
