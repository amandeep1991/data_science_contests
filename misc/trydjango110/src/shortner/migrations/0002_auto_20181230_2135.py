# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-12-30 16:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirrurl',
            name='empty_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 30, 21, 35, 16, 35000)),
        ),
    ]
