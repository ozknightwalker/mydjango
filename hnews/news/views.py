# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse(u"欢迎")


def column_detail(request, column_slug):
    return HttpResponse(u'column detail ' + column_slug)


def artical_detail(request, artical_slug):
    return HttpResponse(u'artical detail!' + artical_slug)