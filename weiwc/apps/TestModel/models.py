# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Test(models.Model):
    user_name = models.CharField(max_length=20)
    user_id = models.IntegerField()
    user_birthday = models.DateField()
