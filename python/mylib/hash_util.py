#!/usr/bin/python
#-*- coding:utf8 -*-
import hashlib

#16进制md5加密,32个大写字符.
def md5(msg):
    m = hashlib.md5()
    m.update(msg)
    return m.hexdigest().upper()
