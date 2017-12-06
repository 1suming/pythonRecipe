#coding:utf-8
'''
Created on 2015-8-30
'''
import sys

def readfile(filename):
    '''print a file to standard output'''
    f=file(filename)
    while True:
        line=f.readline()
        if len(line)==0:
            break;
        print line,
    f.close()

