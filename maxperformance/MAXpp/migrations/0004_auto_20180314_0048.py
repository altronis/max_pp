# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-14 04:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAXpp', '0003_auto_20171011_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='player',
            field=models.CharField(default='admin', max_length=100),
        ),
    ]