# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-04-21 04:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_auto_20160420_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 21, 4, 33, 20, 841889, tzinfo=utc)),
        ),
    ]
