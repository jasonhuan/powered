# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-27 04:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0004_auto_20181127_0443'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_address', models.CharField(max_length=100)),
                ('delivery_fee', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('order_status', models.CharField(default='OP', max_length=2)),
                ('courier_rating', models.IntegerField(blank=True, null=True)),
                ('order_time', models.DateTimeField(auto_now_add=True)),
                ('completion_time', models.DateTimeField(blank=True, null=True)),
                ('courier', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courier', to='profiles.Profile')),
                ('customer', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer', to='profiles.Profile')),
                ('items', models.ManyToManyField(to='categories.OrderItem')),
            ],
        ),
    ]
