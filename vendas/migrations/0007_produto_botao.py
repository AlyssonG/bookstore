# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-23 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0006_rodape_tabela'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='botao',
            field=models.CharField(db_index=True, default='Comprar', max_length=10),
        ),
    ]