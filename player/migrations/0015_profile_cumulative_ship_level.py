# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-04 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0014_auto_20170228_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cumulative_ship_level',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
