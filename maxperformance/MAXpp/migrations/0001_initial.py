# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=100)),
                ('difficulty', models.CharField(max_length=50)),
                ('length_min', models.IntegerField()),
                ('length_sec', models.IntegerField()),
                ('bpm', models.IntegerField()),
                ('star_rating', models.FloatField()),
                ('count_r300', models.IntegerField()),
                ('count_300', models.IntegerField()),
                ('count_200', models.IntegerField()),
                ('count_100', models.IntegerField()),
                ('count_50', models.IntegerField()),
                ('count_0', models.IntegerField()),
                ('acc', models.FloatField()),
                ('max_pp', models.IntegerField()),
                ('pp', models.IntegerField()),
            ],
        ),
    ]
