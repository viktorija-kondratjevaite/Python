# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2019-04-23 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_open',
            field=models.IntegerField(default=0),
        ),
    ]
