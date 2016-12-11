# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-11 03:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0006_port_log'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='port',
            name='log',
        ),
        migrations.AlterField(
            model_name='dockchart',
            name='port',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ports', to='ship.Port'),
        ),
        migrations.AlterField(
            model_name='dockchart',
            name='ship',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ships', to='ship.Ship'),
        ),
    ]