# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('config_descrip', models.CharField(max_length=300)),
                ('tiempo', models.IntegerField(default=15)),
            ],
            options={
                'db_table': 'config_wsn',
                'default_related_name': 'config_wsn',
            },
        ),
        migrations.CreateModel(
            name='Dato',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, db_column='dato_id')),
                ('data', models.FloatField()),
                ('fechahora', models.DateTimeField(verbose_name='')),
            ],
            options={
                'db_table': 'dato',
                'default_related_name': 'dato',
            },
        ),
        migrations.CreateModel(
            name='Locacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, db_column='locacion_id')),
                ('locacion_descrip', models.CharField(max_length=300)),
                ('geom', djgeojson.fields.PointField()),
            ],
            options={
                'db_table': 'locacion',
                'default_related_name': 'locacion',
            },
        ),
        migrations.CreateModel(
            name='Nodo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, db_column='nodo_id')),
                ('nod_descrip', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'nodo',
                'default_related_name': 'nodo',
            },
        ),
        migrations.CreateModel(
            name='Nodo_red',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, db_column='nod_red_id')),
                ('fecha_desde', models.DateField()),
                ('fecha_hasta', models.DateField(null=True, blank=True)),
                ('locacion_id', models.ForeignKey(to='wsn.Locacion', null=True, db_column='locacion_id')),
                ('nod_id', models.ForeignKey(to='wsn.Nodo', db_column='nod_id')),
            ],
            options={
                'db_table': 'nodo_red',
                'default_related_name': 'nodo_red',
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, db_column='rol_id')),
                ('rol_descrip', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'rol',
                'default_related_name': 'rol',
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, db_column='sen_id')),
                ('sen_descrip', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'sensor',
                'default_related_name': 'sensor',
            },
        ),
        migrations.CreateModel(
            name='Tipo_sensor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, db_column='type_sen_id')),
                ('type_sen_descrip', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'tipo_sensor',
                'default_related_name': 'tipo_sensor',
            },
        ),
        migrations.CreateModel(
            name='Wsn',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, db_column='wsn_id')),
                ('wsn_descrip', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'wsn',
                'default_related_name': 'wsn',
            },
        ),
        migrations.AddField(
            model_name='sensor',
            name='type_sen_id',
            field=models.ForeignKey(to='wsn.Tipo_sensor', default=0, db_column='type_sen_id'),
        ),
        migrations.AddField(
            model_name='nodo_red',
            name='rol_id',
            field=models.ForeignKey(to='wsn.Rol', db_column='rol_id'),
        ),
        migrations.AddField(
            model_name='nodo_red',
            name='wsn_id',
            field=models.ForeignKey(to='wsn.Wsn', null=True, db_column='wsn_id'),
        ),
        migrations.AddField(
            model_name='dato',
            name='nod_red_id',
            field=models.ForeignKey(to='wsn.Nodo_red', db_column='nod_red_id'),
        ),
        migrations.AddField(
            model_name='dato',
            name='sen_id',
            field=models.ForeignKey(to='wsn.Sensor', db_column='sen_id'),
        ),
    ]
