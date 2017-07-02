# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import models
# Create your views here.

def add_user(request):
    mo = models.SmUser(user_id=1, user_name="test", user_birthday="2017-01-01 00:00:00")
    mo.save()
    mo = models.SmUserCfg(user_id=1, cfg_if=1)
    mo.save()

    contex = {}
    contex["us"] =  models.SmUser.objects.all()
    contex["title"] = "test title"
    contex["shuchu"] = u"测试输出"
    return render(request, "login/login.html", contex)
