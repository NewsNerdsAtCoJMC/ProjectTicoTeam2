# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-24 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0006_remove_people_apartmentpreferences'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='author',
        ),
        migrations.AddField(
            model_name='apartment',
            name='public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='building',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='name',
            field=models.CharField(default='Test User', max_length=255),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='People',
        ),
    ]