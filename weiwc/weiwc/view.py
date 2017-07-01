#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@author: weiwc
@license: Apache Licence 
@contact: 972237007@qq.com
@site: https://github.com/abelweiwencai
@software: PyCharm Community Edition
@file: view.py.py
@time: 2017/6/30 17:01
"""

# from django.http import HttpResponse:
from django.shortcuts import render
import datetime

def hello(request):
    context = {}
    context["hello"] = "hello world!"
    context["test"] = "test"
    context["tt2"] = ["test","sfd"]
    context["pdate"] = datetime.datetime.now()
    return render(request, "hello.html", context)