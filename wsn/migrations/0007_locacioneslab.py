# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wsn', '0006_datostablalab'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocacionesLab',
            fields=[
                ('locacion_id', models.IntegerField(serialize=False, primary_key=True)),
                ('locacion_descrip', models.TextField()),
                ('geom', djgeojson.fields.PointField()),
            ],
            options={
                'db_table': 'locaciones_lab',
                'managed': False,
                'default_related_name': 'locaciones_lab',
            },
        ),
    ]
