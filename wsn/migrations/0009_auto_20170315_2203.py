# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wsn', '0008_batterylife_datoslab_locacionesnodo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuracion',
            name='tiempo',
            field=models.IntegerField(choices=[(0, '0'), (15, '15'), (45, '45')], default=15),
        ),
    ]
