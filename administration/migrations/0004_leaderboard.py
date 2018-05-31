# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-23 16:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('administration', '0003_delete_mul'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaderBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign_name', models.CharField(blank=True, max_length=100, null=True)),
                ('rank', models.IntegerField(blank=True, null=True)),
                ('referral', models.IntegerField(blank=True, null=True)),
                ('referral_sale', models.IntegerField(blank=True, null=True)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]