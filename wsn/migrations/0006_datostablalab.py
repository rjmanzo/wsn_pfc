# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wsn', '0005_dato_fechahora'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatosTablaLab',
            fields=[
                ('dato_id', models.IntegerField(serialize=False, primary_key=True)),
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
                'db_table': 'datos_tabla_lab',
                'default_related_name': 'datos_tabla_lab',
            },
        ),
    ]
