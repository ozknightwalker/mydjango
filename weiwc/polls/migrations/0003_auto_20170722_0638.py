# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 06:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20170711_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(),
        ),
    ]