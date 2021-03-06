# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 10:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20161213_1634'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='shipstore',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='dock',
            name='slot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slot', to='core.Slot'),
        ),
        migrations.AlterField(
            model_name='dock',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dock', to=settings.AUTH_USER_MODEL),
        ),
    ]
