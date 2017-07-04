#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@author: weiwc
@license: Apache Licence 
@contact: 972237007@qq.com
@site: https://github.com/abelweiwencai
@software: PyCharm Community Edition
@file: py_docs.py
@time: 2017/7/4 21:16
"""
# raw string
print "raw string"
print "abc\nd"
print  r"abc\nd"

print "3*'n'--------"
print 3 * "n" + "a"

print "ab" "cd" "ef"

print u"------- 超过下标的切片不会报错"
print [1, 2, 3, 4][30:]


print u"------- 要再循环一个变量的时候修改这个变量，要先复制"

l = [1, 2, 3, 4]
for x in l[:]:
    if x > 2:
        # l.insert(0, x)
        l.append(x)

print l

print dict(enumerate([1,2,3,4]))
print "-----------------------------------"
import decimal
# 很完整的格式化输出文章，
# http://www.cnblogs.com/RukawaKaede/p/6069977.html
# {0:^25} === 0:第一个参数，<左对齐，>右对齐，^中间对齐 25，最多占用25个字符
fmt = '{0:^25} {1:^25}'
print fmt.format('Input', 'Output')
print fmt.format('-'* 25, '-'* 25 )

# Integer
print fmt.format(5, decimal.Decimal(5))

# String
print fmt.format('3.14', decimal.Decimal('3.14'))

# Float
f = 0.1
print fmt.format(repr(f), decimal.Decimal(str(f)))
print fmt.format('%.23g' % f, str(decimal.Decimal.from_float(f))[:25])



print "-"*60
li = [1, 2, 3, 4, 5, 6]
for x in li:
    print "success", x
    if x > 6:
        print "break"
        continue
else:
    print "for loop sucess"
