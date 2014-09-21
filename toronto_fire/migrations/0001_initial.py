# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('incident_number', models.CharField(unique=True, max_length=30)),
                ('incident_type', models.CharField(default=b'No Type', max_length=255)),
                ('start_datetime', models.DateField(default=django.utils.timezone.now)),
                ('arrival_datetime', models.DateField(default=django.utils.timezone.now)),
                ('end_datetime', models.DateField(default=django.utils.timezone.now)),
                ('alarm_level', models.IntegerField(default=0)),
                ('number_of_units', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
