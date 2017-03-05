from django.db import models
from django.contrib.auth.models import User
from djgeojson.fields import PointField

""" Esta pequeña tabla es agegada al modelo
para guardar las configuraciones de la aplicación """

class Configuracion(models.Model):
    config_descrip = models.CharField(max_length=300)
    tiempo = models.IntegerField(default=15)

    def __str__(self):
        return self.config_descrip

    class Meta:
        db_table = 'config_wsn'
        default_related_name = 'config_wsn'


class Wsn(models.Model):
    id = models.AutoField(primary_key=True, db_column='wsn_id')
    wsn_descrip = models.CharField(max_length=300)

    def __str__(self):
        return self.wsn_descrip

    class Meta:
        db_table = 'wsn'
        default_related_name = 'wsn'


class Nodo(models.Model):
    id = models.AutoField(primary_key=True, db_column='nodo_id')
    nod_descrip = models.CharField(max_length=150)

    def __str__(self):
        return self.nod_descrip

    class Meta:
        db_table = 'nodo'
        default_related_name = 'nodo'


class Rol(models.Model):
    id = models.AutoField(primary_key=True, db_column='rol_id')
    rol_descrip = models.CharField(max_length=50)

    def __str__(self):
        return self.rol_descrip

    class Meta:
        db_table = 'rol'
        default_related_name = 'rol'


class Tipo_sensor(models.Model):
    id = models.AutoField(primary_key=True, db_column='type_sen_id')
    type_sen_descrip = models.CharField(max_length=300)

    def __str__(self):
        return self.type_sen_descrip

    class Meta:
        db_table = 'tipo_sensor'
        default_related_name = 'tipo_sensor'


class Sensor(models.Model):
    id = models.AutoField(primary_key=True, db_column='sen_id')
    type_sen_id = models.ForeignKey(Tipo_sensor, db_column='type_sen_id', default=0)
    sen_descrip = models.CharField(max_length=300)

    def __str__(self):
        return self.sen_descrip + " (" + self.type_sen_id.type_sen_descrip + ")"

    class Meta:
        db_table = 'sensor'
        default_related_name = 'sensor'

class Locacion(models.Model):
    id = models.AutoField(primary_key=True, db_column='locacion_id')
    locacion_descrip = models.CharField(max_length=300)
    geom = PointField()

    def __str__(self):
        return self.locacion_descrip

    @property
    def popupContent(self):
        return self.locacion_descrip

    class Meta:
        db_table = 'locacion'
        default_related_name = 'locacion'

class Nodo_red(models.Model):
    id = models.AutoField(primary_key=True, db_column='nod_red_id')
    nod_id = models.ForeignKey(Nodo, db_column='nod_id')
    rol_id = models.ForeignKey(Rol, db_column='rol_id')
    wsn_id = models.ForeignKey(Wsn, db_column='wsn_id',null=True)
    locacion_id = models.ForeignKey(Locacion, db_column='locacion_id',null=True)
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nod_id.nod_descrip + ' - '+ self.locacion_id.locacion_descrip +' (' + self.rol_id.rol_descrip + ')'  #muestro la descripcion del nodo
    class Meta:
        db_table = 'nodo_red'
        default_related_name = 'nodo_red'

class Dato(models.Model):
    id = models.AutoField(primary_key=True, db_column='dato_id')
    nod_red_id = models.ForeignKey(Nodo_red, db_column='nod_red_id')
    sen_id = models.ForeignKey(Sensor, db_column='sen_id')
    data = models.FloatField()
    fechahora = models.DateTimeField('')

    def __str__(self):
        dato = self.nod_red_id.nod_id.nod_descrip + ' - ' + self.fechahora.strftime("%Y-%m-%d %H:%M:%S")
        return dato

    class Meta:
        db_table = 'dato'
        default_related_name = 'dato'

"""
VISTAS
METODO POCO ELEGANTE PERO FUNCIONAL PARA PODER UTILIZAR VISTAS DE LA BASE DE DATOS
PRECAUCIÓN: PARA PODER EJECUTAR ESTE MODELO HAY QUE HACER LOS SIGUIENTES PASOS:
1. EJECUTAR TODOS LOS MODELOS PREVIOS A ESTE.
2. CREAR LA VIEW EN LA BASE DE DATOS
3. EJECUTAR ESTE MODELO
"""

class DatosTablaLab(models.Model):
    dato_id = models.IntegerField(primary_key=True)
    filtro = models.TextField()
    nodo = models.CharField(max_length=300)
    rol = models.CharField(max_length=300)
    locacion = models.CharField(max_length=300)
    tipo_sensor = models.CharField(max_length=300)
    sensor = models.CharField(max_length=300)
    data = models.FloatField()
    fecha_hora = models.DateTimeField()
    fecha_hora_text = models.TextField()

    def __str__(self):
        dato = self.nodo +" ("+self.locacion+ ") - " + self.fecha_hora.strftime("%Y-%m-%d %H:%M:%S")
        return dato

    class Meta:
        managed = False
        db_table = 'datos_tabla_lab'
        default_related_name = 'datos_tabla_lab'

class LocacionesLab(models.Model):
    locacion_id = models.IntegerField(primary_key=True)
    locacion_descrip = models.TextField()
    geom = PointField()

    def __str__(self):
        return self.locacion_descrip

    class Meta:
        managed = False
        db_table = 'locaciones_lab'
        default_related_name = 'locaciones_lab'
