# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sm_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmUserCfg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('cfg_if', models.IntegerField()),
            ],
        ),
    ]
