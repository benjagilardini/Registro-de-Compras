# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-09-12 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now=True, verbose_name='Fecha')),
                ('compra', models.CharField(max_length=100)),
            ],
        ),
    ]
