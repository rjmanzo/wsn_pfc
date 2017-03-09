from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeoModelSerializer
from wsn.models import Nodo_red,Sensor,Dato,Configuracion, DatosTablaLab, LocacionesLab

"""Comunicacion wsn"""
class NodoRedSerializers(serializers.ModelSerializer):
   class Meta:
       model = Nodo_red
       """fields = ('id','nod_red_descrip')"""
       fields = '__all__'

class SensorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id','sen_descrip')
        """fields = '__all__'"""

class DatoSerializers(serializers.ModelSerializer):
    nod_red_id = NodoRedSerializers()
    sen_id = SensorSerializers()

    class Meta:
        model = Dato
        fields = ('id','data','nod_red_id','sen_id', 'fechahora')

"""test numero uno. PERFECTOOOO.... ANDA EL HDP!!!"""
class ConfiguracionSerializers(serializers.ModelSerializer):
   class Meta:
       model = Configuracion
       fields = ('id', 'tiempo')
       """fields = ('id', 'config_descrip','tiempo')"""

"""Serializamos la vista de datos para poder utilizarla en las gráficas"""
class DatosTablaLabSerializers(serializers.ModelSerializer):
    """cambio el formato del timestamp para poder usarlo en las graficas (Python format type)"""
    timestamp = serializers.DateTimeField(source='fecha_hora', format="%Y-%m-%d %H:%M:%S")

    class Meta:
         model = DatosTablaLab
         fields = ('filtro','data','timestamp')
         read_only_fields = ('filtro','data','timestamp')

#"""Serializamos la vista de locaciones lab para poder utilizarla en el mapa"""
class LocacionesLabSerializers(GeoFeatureModelSerializer):

    class Meta:
        model = LocacionesLab
        """#Gis  field"""
        geo_field = 'geom'
        """ id_field = False"""

        fields = ('locacion_id','locacion_descrip')
