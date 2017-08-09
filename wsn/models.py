from django.db import models
from django.contrib.auth.models import User
from djgeojson.fields import PointField
from django_pgviews import view as pg
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# This code is triggered whenever a new user has been created and saved to the database
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

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
        return self.nod_id.nod_descrip + ' - '+ self.locacion_id.locacion_descrip +' (' + self.rol_id.rol_descrip +  ')'  #muestro la descripcion del nodo
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

""" En esta tabla se guardan las configuraciones
de los distintos nodos de la red """

class Configuracion_wsn(models.Model):
    OFF = 99
    QUINCE = 1
    MEDIA = 2
    CUARENTAYCINCO = 3
    UNAHORA = 4
    DOSHORAS = 5
    CUATROHORAS = 6
    SEISHORAS = 7
    DOCEHORAS = 8
    UNDIA = 9
    TIEMPOS = (
        (OFF, 'APAGADO'),
        (QUINCE, '15 MIN'),
        (MEDIA, '30 MIN'),
        (CUARENTAYCINCO, '45 MIN'),
        (UNAHORA, 'UNA HORA (60 MIN)'),
        (DOSHORAS, 'DOS HORAS (120 MIN)'),
        (CUATROHORAS, 'CUATRO HORAS (240 MIN)'),
        (SEISHORAS, 'SEIS HORAS (360 MIN)'),
        (DOCEHORAS, 'DOCE HORAS (720 MIN)'),
        (UNDIA, 'DIA (24 HRS)'),
    )

    id = models.AutoField(primary_key=True, db_column='config_id')
    tiempo = models.IntegerField(choices = TIEMPOS , default = QUINCE)
    nod_red_id = models.ForeignKey(Nodo_red, db_column='nod_red_id', null=True)
    sen_id = models.ForeignKey(Sensor, db_column='sen_id',null=True)
    config_descrip = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.nod_red_id.nod_id.nod_descrip + ' (' + self.nod_red_id.wsn_id.wsn_descrip + ') - ' + self.sen_id.sen_descrip + ' (' + self.sen_id.type_sen_id.type_sen_descrip + ')'

    class Meta:
        db_table = 'configuracion_wsn'
        default_related_name = 'configuracion_wsn'

"""
modelos construidos en base a vistas Postgre ---------------------------------------
"""

"""SQL BatteryLife model """
VIEW_SQL_BAT = """
    SELECT  d.dato_id,
            ((n.nod_descrip::text || '('::text) || l.locacion_descrip::text) || ')'::text AS nodo,
            w.wsn_id,
            w.wsn_descrip,
            d.data,
            d.fechahora AS fecha_hora

    FROM dato d
    LEFT JOIN nodo_red nr ON nr.nod_red_id = d.nod_red_id
    LEFT JOIN wsn w ON w.wsn_id = nr.wsn_id
    LEFT JOIN nodo n ON n.nodo_id = nr.nod_id
    LEFT JOIN sensor s ON s.sen_id = d.sen_id
    LEFT JOIN tipo_sensor ts ON ts.type_sen_id = s.type_sen_id
    LEFT JOIN locacion l ON l.locacion_id = nr.locacion_id
    WHERE s.sen_descrip = 'Tensión'
"""

"""BatteryLife model """
class BatteryLife(pg.View):
    dato_id = models.IntegerField(primary_key=True)
    nodo = models.TextField()
    wsn_id = models.IntegerField()
    wsn_descrip = models.CharField(max_length=300)
    data = models.FloatField()
    fecha_hora = models.DateTimeField()
    #projection = ['dato.*',]
    #dependencies = ['myapp.OtherView',]
    sql = VIEW_SQL_BAT

    def __str__(self):
        dato = self.nodo +' [' +'] ' +self.fecha_hora.strftime("%Y-%m-%d %H:%M:%S")
        return dato

    class Meta:
        #app_label = 'myapp'
        db_table = 'battery_life'
        default_related_name = 'battery_life'
        managed = False

"""SQL Datos test-lab-uno model """
VIEW_SQL_TDLAB_UNO = """
    SELECT  d.dato_id,
            n.nod_descrip||'_'||ts.type_sen_descrip||'_'||s.sen_descrip as filtro,
            n.nod_descrip as nodo,
            r.rol_descrip as rol,
            l.locacion_descrip as locacion,
            ts.type_sen_descrip as tipo_sensor,
            s.sen_descrip as sensor,
            d.data,
            d.fechahora as fecha_hora,
            to_char(fechahora AT TIME ZONE 'UTC+3', 'YYYY-MM-DD HH24:MI:SS') as fecha_hora_text

    FROM dato d
    LEFT JOIN nodo_red nr ON nr.nod_red_id = d.nod_red_id
    LEFT JOIN rol r ON r.rol_id = nr.rol_id
    LEFT JOIN wsn w ON w.wsn_id = nr.wsn_id
    LEFT JOIN nodo n ON n.nodo_id = nr.nod_id
    LEFT JOIN sensor s ON s.sen_id = d.sen_id
    LEFT JOIN tipo_sensor ts ON ts.type_sen_id = s.type_sen_id
    LEFT JOIN locacion l ON l.locacion_id = nr.locacion_id
    where w.wsn_id = 1 --wsn: Prueba de Laboratorio Nro. 1
"""

"""Datos test-lab-uno model """
class DatosLabUno(pg.View):
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
    #projection = ['dato.*',]
    #dependencies = ['myapp.OtherView',]
    sql = VIEW_SQL_TDLAB_UNO

    def __str__(self):
        dato = self.nodo +" ("+self.locacion+ ") - " + self.fecha_hora.strftime("%Y-%m-%d %H:%M:%S")
        return dato

    class Meta:
        #app_label = 'myapp'
        db_table = 'datos_lab'
        default_related_name = 'datos_lab'
        managed = False

"""SQL locacionesNodo model """
VIEW_SQL_LOC = """
SELECT  l.locacion_id,
            n.nod_descrip||'('|| l.locacion_descrip ||')' as locacion_descrip,
            w.wsn_descrip,
            l.geom

FROM nodo_red nr
LEFT JOIN wsn w ON w.wsn_id = nr.wsn_id
LEFT JOIN nodo n ON n.nodo_id = nr.nod_id
LEFT JOIN locacion l ON l.locacion_id = nr.locacion_id
WHERE nr.fecha_hasta is null
"""

""" locacionesNodo model """
class LocacionesNodo(pg.View):
    locacion_id = models.IntegerField(primary_key=True)
    locacion_descrip = models.TextField()
    wsn_descrip = models.CharField(max_length=300)
    geom = PointField()
    #projection = ['dato.*',]
    #dependencies = ['myapp.OtherView',]
    sql = VIEW_SQL_LOC

    def __str__(self):
        return self.locacion_descrip

    class Meta:
        #app_label = 'myapp'
        db_table = 'locaciones_nodos'
        default_related_name = 'locaciones_nodos'
        managed = False

    @property
    def popupContent(self):
      return self.locacion_descrip

"""SQL test-campo-uno model """
VIEW_SQL_TDCAMPO_UNO = """
    SELECT  d.dato_id,
            n.nod_descrip||'_'||ts.type_sen_descrip||'_'||s.sen_descrip as filtro,
            n.nod_descrip as nodo,
            r.rol_descrip as rol,
            l.locacion_descrip as locacion,
            ts.type_sen_descrip as tipo_sensor,
            s.sen_descrip as sensor,
            d.data,
            d.fechahora as fecha_hora,
            to_char(fechahora AT TIME ZONE 'UTC+3', 'YYYY-MM-DD HH24:MI:SS') as fecha_hora_text

    FROM dato d
    LEFT JOIN nodo_red nr ON nr.nod_red_id = d.nod_red_id
    LEFT JOIN rol r ON r.rol_id = nr.rol_id
    LEFT JOIN wsn w ON w.wsn_id = nr.wsn_id
    LEFT JOIN nodo n ON n.nodo_id = nr.nod_id
    LEFT JOIN sensor s ON s.sen_id = d.sen_id
    LEFT JOIN tipo_sensor ts ON ts.type_sen_id = s.type_sen_id
    LEFT JOIN locacion l ON l.locacion_id = nr.locacion_id
    where w.wsn_id = 2 --wsn: Pruebas de campo Nro. 1
"""

""" test-campo-uno model """
class DatosCampoUno(pg.View):
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
    #projection = ['dato.*',]
    #dependencies = ['myapp.OtherView',]
    sql = VIEW_SQL_TDCAMPO_UNO

    def __str__(self):
        dato = self.nodo +" ("+self.locacion+ ") - " + self.fecha_hora.strftime("%Y-%m-%d %H:%M:%S")
        return dato

    class Meta:
        #app_label = 'myapp'
        db_table = 'datos_campo_uno'
        default_related_name = 'datos_campo_uno'
        managed = False

#Los modelos (pg.views) que faltan:
#DatosLabDos
#DatosCampoDos
