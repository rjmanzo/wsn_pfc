# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wsn', '0007_locacioneslab'),
    ]

    operations = [
        migrations.CreateModel(
            name='BatteryLife',
            fields=[
                ('dato_id', models.IntegerField(serialize=False, primary_key=True)),
                ('nodo', models.TextField()),
                ('wsn_id', models.IntegerField()),
                ('wsn_descrip', models.CharField(max_length=300)),
                ('data', models.FloatField()),
                ('fecha_hora', models.DateTimeField()),
            ],
            options={
                'default_related_name': 'battery_life',
                'managed': False,
                'db_table': 'battery_life',
            },
        ),
        migrations.CreateModel(
            name='DatosLab',
            fields=[
                ('dato_id', models.IntegerField(serialize=False, primary_key=True)),
                ('filtro', models.TextField()),
                ('nodo', models.CharField(max_length=300)),
                ('rol', models.CharField(max_length=300)),
                ('locacion', models.CharField(max_length=300)),
                ('tipo_sensor', models.CharField(max_length=300)),
                ('sensor', models.CharField(max_length=300)),
                ('data', models.FloatField()),
                ('fecha_hora', models.DateTimeField()),
                ('fecha_hora_text', models.TextField()),
            ],
            options={
                'default_related_name': 'datos_lab',
                'managed': False,
                'db_table': 'datos_lab',
            },
        ),
        migrations.CreateModel(
            name='LocacionesNodo',
            fields=[
                ('locacion_id', models.IntegerField(serialize=False, primary_key=True)),
                ('locacion_descrip', models.TextField()),
                ('wsn_descrip', models.CharField(max_length=300)),
                ('geom', djgeojson.fields.PointField()),
            ],
            options={
                'default_related_name': 'locaciones_nodos',
                'managed': False,
                'db_table': 'locaciones_nodos',
            },
        ),
    ]
