#coding:utf-8
'''
Created on 2015-8-30
'''
#求10的阶乘
print reduce(lambda x,y:x*y,range(1,11))

def bubble(x,n):
    """
    冒泡排序，x是列表，n是长度
    """
    for i in range(n):
        for j in range(n-1):
            if x[j]>x[j+1]:
                t=x[j]
                x[j]=x[j+1]
                x[j+1]=t
    return x

print bubble([1,10,2,5],4)

#插入排序
def insertSort(x,n):
    for i in range(1,n):
        key=x[i]
        j=i-1
        while j>=0 and key<x[j]:
            x[j+1]=x[j]
            j-=1
        x[j+1]=key
        
    return x
print insertSort([1,10,2,5,4],5)

def insertRec(x,n):
    if n==1:
        return
    insertRec(x,n-1)
    key=x[n-1]
    i=n-2
    while i>=0 and x[i]>key:
        x[i+1]=x[i]
        i-=1
    x[i+1]=key
    
ls=[1,5,2,7,4]
insertRec(ls,5)
print ls

    

    
        
#选择排序
def selectSort(x,n):
    for i in range(0,n-1): #[0,n-2]
        maxValue=x[i]
        maxKey=i
        for j in range(i+1,n):#[i+1,n-1]   
            if(x[j]>maxValue):
                maxValue=x[j]
                maxKey=j
        if(i!=maxKey):
            x[i],x[maxKey]=x[maxKey],x[i]
    return x

print selectSort([1,10,2,5,4],5)
       

            
        
        