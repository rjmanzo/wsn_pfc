# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wsn', '0018_auto_20170810_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatosYachtclub',
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
                'default_related_name': 'datos_yachtclub',
                'db_table': 'datos_yachtclub',
            },
        ),
    ]
