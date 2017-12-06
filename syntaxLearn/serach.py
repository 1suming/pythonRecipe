#coding:utf-8
'''
Created on 2015-8-30
'''

#horner's霍纳规则x[0],x[1],n is length
def horner(x,n,k):
    y=0
    i=n-1
    while i>=0:
        y=x[i]+y*k
        i-=1
    return y 

def hornerTest():
    x=[1,2,3]
    n=3
    k=2
    print horner(x,n,k)
hornerTest()
        
        