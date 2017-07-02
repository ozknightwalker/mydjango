#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@author: weiwc
@license: Apache Licence 
@contact: 972237007@qq.com
@site: https://github.com/abelweiwencai
@software: PyCharm Community Edition
@file: search.py
@time: 2017/7/2 12:58
"""

from django.http import HttpResponse
from apps.TestModel import models
from django.shortcuts import render_to_response

# 表单
def search_form(request):
    return render_to_response("search_form.html")

# 接受请求数据
def search(request):
    response = ""
    request.encoding = "utf-8"
    if 'q' in request.GET:
        message = u"你搜索的内容为：" + request.GET["q"]
    else:
        message = u"请输入搜索内容："

    return HttpResponse(message)

    return HttpResponse("ok")



def main():
    pass


if __name__ == '__main__':
    main()