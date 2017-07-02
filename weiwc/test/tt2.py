#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@author: weiwc
@license: Apache Licence 
@contact: 972237007@qq.com
@site: https://github.com/abelweiwencai
@software: PyCharm Community Edition
@file: tt2.py
@time: 2017/7/2 7:51
"""


def main():
    list1 = list(xrange(10))
    print list1
    tm2 = zip(list1)
    print tm2
    tm3 = map(lambda x:x[0], tm2)
    print tm3
    tm4 = [filter(lambda x : x/2, list1)]
    print tm4


if __name__ == '__main__':
    main()
