#coding:utf-8
'''
Created on 2015-11-14
'''
from urllib import *

data={'a':'test','name':'我'}
print 'data:',urlencode(data)
print quote('我')