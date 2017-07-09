#!/usr/bin/env python
# encoding: utf-8

"""
@version: python2.7
@author: weiwc
@license: Apache Licence
@contact: 972237007@qq.com
@site: https://github.com/abelweiwencai
@software: PyCharm Community Edition
@file: std_lib.py
@time: 2017/7/9 13:51
"""
import os

import struct

data = open('myfile.zip', 'rb').read()
start = 0
for i in range(3):
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start + 16])
    crc32, comp_size, uncompack_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start + filenamesize]
