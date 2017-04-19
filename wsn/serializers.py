from rest_framework import serializers
from wsn.models import Nodo_red,Sensor,Dato,Configuracion_wsn, BatteryLife, DatosLabUno, DatosCampoUno

"""Comunicacion wsn"""
class NodoRedSerializers(serializers.ModelSerializer):
   class Meta:
       model = Nodo_red
       fields = '__all__'
       #fields = ('id','nod_red_descrip')

class SensorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'
        #fields = ('id','sen_descrip')

class DatoSerializers(serializers.ModelSerializer):
    #nod_red_id = NodoRedSerializers()
    #sen_id = SensorSerializers()

    class Meta:
        model = Dato
        fields = '__all__'
        #fields = ('id','data','nod_red_id','sen_id', 'fechahora')

"""Configuracion_wsn"""
class ConfiguracionSerializers(serializers.ModelSerializer):
   class Meta:
       model = Configuracion_wsn
       fields = '__all__'
       #fields = ('id', 'config_descrip','tiempo')


"""Serializamos la vista de datos para poder utilizarla en las gráficas"""
class DatosTablaLabUnoSerializers(serializers.ModelSerializer):
    """cambio el formato del timestamp para poder usarlo en las graficas (Python format type)"""
    timestamp = serializers.DateTimeField(source='fecha_hora', format="%Y-%m-%d %H:%M:%S")

    class Meta:
         model = DatosLabUno
         fields = ('filtro','data','timestamp')
         read_only_fields = ('filtro','data','timestamp')

"""Serializamos la vista de datos para poder utilizarla en las gráficas"""
class DatosTablaCampoUnoSerializers(serializers.ModelSerializer):
    """cambio el formato del timestamp para poder usarlo en las graficas (Python format type)"""
    timestamp = serializers.DateTimeField(source='fecha_hora', format="%Y-%m-%d %H:%M:%S")

    class Meta:
         model = DatosCampoUno
         fields = ('filtro','data','timestamp')
         read_only_fields = ('filtro','data','timestamp')
