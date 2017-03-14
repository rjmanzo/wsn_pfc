from django.contrib import admin
from wsn.models import (
    Nodo,Nodo_red,Dato,Sensor,
    Rol,Tipo_sensor,Wsn,Configuracion,Locacion,
    BatteryLife,DatosLab,LocacionesNodo
)
from leaflet.admin import LeafletGeoAdmin

"""#Tablas del modelo"""
admin.site.register(Nodo)
admin.site.register(Nodo_red)
admin.site.register(Sensor)
admin.site.register(Dato)
admin.site.register(Tipo_sensor)
admin.site.register(Wsn)
admin.site.register(Rol)
admin.site.register(Configuracion)

"""#mapas"""
admin.site.register(Locacion, LeafletGeoAdmin)

"""#Vistas"""
admin.site.register(BatteryLife)
admin.site.register(DatosLab)
admin.site.register(LocacionesNodo, LeafletGeoAdmin)
