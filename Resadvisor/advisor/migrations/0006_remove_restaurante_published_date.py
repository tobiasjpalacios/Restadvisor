# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-13 13:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0005_auto_20171009_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurante',
            name='published_date',
        ),
    ]
