# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toronto_fire', '0002_auto_20140921_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='duration_in_min',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
