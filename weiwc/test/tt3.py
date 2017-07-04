#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@author: weiwc
@license: Apache Licence 
@contact: 972237007@qq.com
@site: https://github.com/abelweiwencai
@software: PyCharm Community Edition
@file: tt3.py
@time: 2017/7/3 16:16
"""
import collections

print "nametuple"
point = collections.namedtuple("po",["x", "y", "z"])
a = point(1, 2, 3)
print a.x, a.y, a.z

b = collections.defaultdict()
c = collections.OrderedDict()

x =  list(range(10))
z = {k: y for (k, y) in zip(x, x)}
print z


print "deque-----"
a = collections.deque([1, 2, 3, 4, 5])
a.append(6)
a.appendleft(0)
print a



class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, sc = 0):
        self._score = sc

s = Student()
s.score = 10
print s.score
s.score = 20



