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

    all_user = models.Test.objects.all()

    tt = models.Test.objects.get(id=2)
    models.Test.objects.filter(id=1)
    models.Test.objects.order_by("id")
    tt = models.Test.objects.order_by("name")[0:2]

    models.Test.objects.filter(id=1).update(user_name="test")

    # models.Test.objects.filter(id=1).delete()


    response = "--"
    for user in all_user:
        user.user_name = "weiwc" + str(user.id)
        user.user_id = user.id
        user.save()
        #
        # response += "<li>"
        # response += "id="+ str(user.id)
        # response += "  name="+ user.user_name
        # response += "<li/>"


    return HttpResponse(response)


def main():
    pass


if __name__ == '__main__':
    main()