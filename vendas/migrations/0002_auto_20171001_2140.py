# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 00:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produtos', to='vendas.Categoria'),
        ),
    ]
