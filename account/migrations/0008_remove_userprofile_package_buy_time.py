# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-21 13:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_userprofile_payments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='package_buy_time',
        ),
    ]
