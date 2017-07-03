#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@author: weiwc
@license: Apache Licence 
@contact: 972237007@qq.com
@site: https://github.com/abelweiwencai
@software: PyCharm Community Edition
@file: test_singleton.py
@time: 2017/7/3 11:00
"""

def singleton(cls, *args, **kw):
    instance = {}
    def _singleton():
        if cls not in instance:
            instance[cls] = cls(*args, **kw)
        return instance[cls]
    return _singleton

@singleton
class MyClass():
    def __init__(self):
        self.dd = 1

a = MyClass()
b = MyClass()
print(id(a))
print(id(b))
a.dd = 2
print(a.dd, b.dd)
a.dd = 3
print(a.dd, b.dd)
b.dd = 2
print(a.dd, b.dd)
b.dd = 3
print(a.dd, b.dd)




def singleton1(cls, *args, **kw):
    instance = {}
    def _singleton():
        if cls not in instance:
            instance[cls] = cls(*args, **kw)
        return instance[cls]
    return _singleton

@singleton1
class MyClass1():
    def __init__(self):
        self.dd = 1

k = MyClass1()
print(id(k), k.dd)