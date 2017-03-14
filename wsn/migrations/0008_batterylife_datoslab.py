# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wsn', '0007_locacioneslab'),
    ]

    operations = [
        migrations.CreateModel(
            name='BatteryLife',
            fields=[
                ('dato_id', models.IntegerField(primary_key=True, serialize=False)),
                ('nodo', models.TextField()),
                ('red_id', models.IntegerField()),
                ('data', models.FloatField()),
                ('fecha_hora', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'default_related_name': 'battery_life',
                'db_table': 'battery_life',
            },
        ),
        migrations.CreateModel(
            name='DatosLab',
            fields=[
                ('dato_id', models.IntegerField(primary_key=True, serialize=False)),
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
                'managed': False,
                'default_related_name': 'datos_lab',
                'db_table': 'datos_lab',
            },
        ),
    ]
