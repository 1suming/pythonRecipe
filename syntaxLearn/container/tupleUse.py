#!/usr/bin/python
#coding: utf-8

t=(1,2)

emptyTuple =()

#1个元素的元祖，为了避免括号歧义，必须加逗号 ,元组是有逗号决定的，不是由括号决定
oneTuple=(1,)
print(type(oneTuple))

t5=('a','b',['A','B'])
t5[2][0]='X'

print(t5)

#任意无符号的对象，以逗号分隔，默认为元组 ,
a=1,2
print(type(a))

x,y=1,2

#list-->tuple
lst=[1,2,3]
lstToTuple = tuple(lst)
print(lstToTuple)

