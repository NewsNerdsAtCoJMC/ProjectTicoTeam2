# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0002_auto_20170314_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='distanceToCity',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='building',
            name='distanceToEast',
            field=models.FloatField(),
        ),
    ]
