# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-23 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0004_leaderboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaderboard',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='leaderboard',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
