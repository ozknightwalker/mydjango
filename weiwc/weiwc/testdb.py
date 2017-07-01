#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@author: weiwc
@license: Apache Licence 
@contact: 972237007@qq.com
@site: https://github.com/abelweiwencai
@software: PyCharm Community Edition
@file: testdb.py
@time: 2017/7/1 20:49
"""
from django.http import HttpResponse
from apps.TestModel import models


def testdb(request):

    insert_data = models.Test(user_name="weiwc", user_id=1, user_birthday="2017-01-01")
    insert_data.save()
    return HttpResponse("<p>插入数据城功！<p/>")


def main():
    pass


if __name__ == '__main__':
    main()