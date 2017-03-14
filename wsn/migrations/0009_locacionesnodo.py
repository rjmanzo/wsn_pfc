# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wsn', '0008_batterylife_datoslab'),
    ]

    operations = [
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
