# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurante',
            name='title',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]