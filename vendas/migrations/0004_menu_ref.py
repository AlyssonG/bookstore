# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-23 20:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0003_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='ref',
            field=models.CharField(blank=True, db_index=True, max_length=20),
        ),
    ]
