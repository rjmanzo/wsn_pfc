# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('wsn', '0002_remove_dato_fechahora'),
    ]

    operations = [
        migrations.AddField(
            model_name='dato',
            name='fechahora',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 22, 11, 41, 23, 815757, tzinfo=utc), verbose_name=''),
            preserve_default=False,
        ),
    ]
