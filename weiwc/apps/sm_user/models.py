# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your models here.

from  django.db import models

class SmUser(models.Model):
    user_id = models.IntegerField(max_length=8)
    user_name = models.CharField(max_length=32)
    user_birthday = models.DateTimeField()

class SmUserCfg(models.Model):
    user_id = models.IntegerField()
    cfg_if = models.IntegerField()