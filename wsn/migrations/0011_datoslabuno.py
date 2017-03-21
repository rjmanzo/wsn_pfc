# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wsn', '0010_configuracion_wsn'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatosLabUno',
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
                'db_table': 'datos_lab',
                'managed': False,
            },
        ),
    ]
