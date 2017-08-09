# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wsn', '0014_auto_20170809_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuracion_wsn',
            name='tiempo',
            field=models.IntegerField(choices=[(254, 'APAGADO'), (1, '15 MIN'), (2, '30 MIN'), (3, '45 MIN'), (4, 'UNA HORA (60 MIN)'), (5, 'DOS HORAS (120 MIN)'), (6, 'CUATRO HORAS (240 MIN)'), (7, 'SEIS HORAS (360 MIN)'), (8, 'DOCE HORAS (720 MIN)'), (9, 'DIA (24 HRS)')], default=1),
        ),
    ]
