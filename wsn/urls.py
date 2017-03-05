from django.conf.urls import include, url
from . import views
"""Necesario agregar el nombre de la app para el uso de URL namespace"""

app_name = 'wsn'

urlpatterns = [
    url(
        regex='^wsn/main/$',
        view= views.main_page,
        name= 'starter'
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
        regex='^api-locations-lab/$',
        view= views.LocacionesLabList.as_view(),
        name= 'api_locations_lab'
    ),
    url(
        regex='^api-table-lab',
        view = views.TablaLabsListJson.as_view(),
        name='tabla_lab_list_json'
    ),
]
