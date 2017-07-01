#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@author: weiwc
@license: Apache Licence 
@contact: 972237007@qq.com
@site: https://github.com/abelweiwencai
@software: PyCharm Community Edition
@file: tt_conn_mysql.py
@time: 2017/7/1 12:10
"""




#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","weiwc","weiwc", "weiwc")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print ("Database version : %s " % data)

# 关闭数据库连接
db.close()