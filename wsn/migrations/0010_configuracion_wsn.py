# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wsn', '0009_delete_configuracion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracion_wsn',
            fields=[
                ('id', models.AutoField(primary_key=True, db_column='config_id', serialize=False)),
                ('tiempo', models.IntegerField(choices=[(-1, 'APAGADO'), (1, '15 MIN'), (2, '30 MIN'), (3, '45 MIN'), (4, 'UNA HORA (60 MIN)'), (5, 'DOS HORAS (120 MIN)'), (6, 'CUATRO HORAS (240 MIN)'), (7, 'SEIS HORAS (360 MIN)'), (8, 'DOCE HORAS (720 MIN)'), (9, 'DIA (24 HRS)')], default=1)),
                ('config_descrip', models.CharField(max_length=300, blank=True)),
                ('nod_red_id', models.ForeignKey(null=True, db_column='nod_red_id', to='wsn.Nodo_red')),
                ('sen_id', models.ForeignKey(null=True, db_column='sen_id', to='wsn.Sensor')),
            ],
            options={
                'db_table': 'configuracion_wsn',
                'default_related_name': 'configuracion_wsn',
            },
        ),
    ]
