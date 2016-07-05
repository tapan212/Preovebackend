# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 09:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_appuser_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quickstart', to=settings.AUTH_USER_MODEL),
        ),
    ]
