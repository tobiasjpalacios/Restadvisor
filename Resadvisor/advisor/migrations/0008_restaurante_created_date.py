# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-13 13:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0007_auto_20171013_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurante',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
