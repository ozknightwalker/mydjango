# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('user_id', models.IntegerField(max_length=8)),
                ('user_birthday', models.DateField()),
            ],
        ),
    ]
