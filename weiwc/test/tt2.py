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
    list2 = list(xrange(10, 20))
    list3 = list(xrange(20, 30))
    print list1
    tm2 = zip(list1)
    print tm2
    tm3 = map(lambda x:x[0], tm2)
    print tm3
    tm4 = [filter(lambda x : x/2, list1)]
    print "tm4", tm4
    tt1 = zip(list1, list2, list3)
    print tt1
    tt2 = zip(*tt1)
    print "tt2", tt2
    d = zip(*tt1)
    x = d[0]
    y = d[1]
    z = d[2]
    print x, y, z
    import heapq

    rr0 = zip(list2,list1)
    print "rr0", rr0
    for x in rr0:
        print x
    print "rr0", rr0

    rr = dict(zip(list1,list2))
    print rr
    rr2 = dict(rr0)
    print rr2
    print dict([["a",1],["b",2]])

    kk = heapq.nlargest(2, [1,2,3,4,5])
    print kk



if __name__ == '__main__':
    main()
