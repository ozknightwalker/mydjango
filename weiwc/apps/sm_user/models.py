# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models

# Create your models here.


class SmUser(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=32)
    user_birthday = models.DateTimeField()


class SmUserCfg(models.Model):
    user_id = models.IntegerField()
    cfg_if = models.IntegerField()