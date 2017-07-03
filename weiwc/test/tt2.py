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
    print(list1)
    tm2 = zip(list1)
    print(tm2)
    print("map----")
    tm3 = map(lambda x:x[0], tm2)
    print( tm3)
    print("filter----")
    tm4 = [filter(lambda x : x/2, list1)]
    print ("tm4", tm4)
    print("zip----")
    tt1 = zip(list1, list2, list3)
    print(tt1)
    print("unzip----")
    tt2 = zip(*tt1)
    print("tt2", tt2)
    d = zip(*tt1)
    x = d[0]
    y = d[1]
    z = d[2]
    print( x, y, z)
    import heapq

    rr0 = zip(list2,list1)
    print("rr0", rr0)
    for x in rr0:
        print(x)
    print("rr0", rr0)

    rr = dict(zip(list1,list2))
    print(rr)
    rr2 = dict(rr0)
    print(rr2)
    print(dict([["a",1],["b",2]]))
    print("heapq----")
    kk = heapq.nlargest(2, [1,2,3,4,5])
    print(kk)
    print("reduce")
    print(reduce(lambda x, y: x+y, range(1,101)))


    print("-----------------------------")
    # 赋值
    print(u"赋值-不可变对象")
    a = 1
    b = a
    print("a=", a)
    print("b=", b)
    print("---------------")
    a = a + 1  # int 为不可变对象，a的指向变了 a != b
    print("a=", a)
    print("b=", b)
    print("---------------")

    print(u"赋值-可变对象")
    a = list(range(3))
    b = a  # b 引用a 相当于指针
    print("a=", a)
    print("b=", b)
    print("---------------")
    a.append(4)  # 虽然是append，b的值也随之改变，a == b
    print("a=", a)
    print("b=", b)
    print("---------------")

    from copy import copy, deepcopy
    # 浅拷贝
    print(u"浅拷贝")
    a = list(range(3))
    a.append([1, 2])
    b = copy(a)
    print("a=", a)
    print("b=", b)
    print("---------------")
    a.append(1)
    print("a=", a)
    print("b=", b)
    print("---------------")
    a[3].append(3)
    print("a=", a)
    print("b=", b)
    print("---------------")

    # 深拷贝
    print(u"深拷贝")
    a = list(range(3))
    a.append([1, 2])
    b = deepcopy(a)
    print(a, b)
    a.append(1)
    print("a=", a)
    print("b=", b)
    print("---------------")
    a[3].append(3)
    print("a=", a)
    print("b=", b)
    print("---------------")
    import random
    print(random.randint(1,2))


def lo(func):
    def wrapper(*args, **kw):
        print("在装饰器里面")
        f = func(*args, **kw)
        print("在装饰器之后")
        # return f  # 这里返回的是函数结果
    return wrapper  # 这里返回的是函数对象

@lo
def tp():
    print("函数")
    return "haha"



if __name__ == '__main__':
    # main()
    a = tp()
    print("a=", a)
