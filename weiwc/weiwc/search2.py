#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@author: weiwc
@license: Apache Licence 
@contact: 972237007@qq.com
@site: https://github.com/abelweiwencai
@software: PyCharm Community Edition
@file: search2.py
@time: 2017/7/2 14:09
"""

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf

def search_post(request):
    ctx = {}
    if request.POST:
        ctx["rlt"] = request.POST["q"]
    return render(request, "post.html", ctx)

def main():
    pass


if __name__ == '__main__':
    main()