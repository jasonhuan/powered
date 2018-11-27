# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-27 04:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_auto_20181117_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderplace',
            name='lat',
            field=models.DecimalField(decimal_places=7, default=0.0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderplace',
            name='lng',
            field=models.DecimalField(decimal_places=7, default=0.0, max_digits=10),
            preserve_default=False,
        ),
    ]