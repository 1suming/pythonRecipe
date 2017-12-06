#coding:utf-8
'''
Created on 2015-10-29
'''
import collections

#方法1，使用OrderedDict ''不能存储可变类型对象，不能并发访问set()'''
class LRUCache:
    #@param capacity,an integer
    def __init__(self,capacity):
        self.capacity=capacity
        self.length=0
        self.dict=collections.OrderedDict() #后加入的一定排在先加入的后面
    def get(self,key):
        try:
            value=self.dict[key]
            del self.dict[key]
            self.dict[key]=value
            return value
        
        except:
            return -1
        
    def set(self,key,value):
        try:
            del self.dict[key]
            self.dict[key]=value
        except:
            if self.length==self.capacity:
                self.dict.popitem(last=False) #弹出头部元素
                self.length-=1
            self.dict[key]=value
            self.length+=1
          
#用dict+list实现  
class LRUCache2:
    alist=[] #基于普通的dict
    dict={}
    
    def __init__(self,capacity):
        self.capacity=capacity
        
    def get(self,key):
        if self.dict.has_key(key):
            value=self.dict[key]
            self.alist.remove(key)
            self.alist.insert(0,key) #最近访问插入头部
        else:
            value=None
            
        return value
    
    def set(self,key,value):
        if self.dict.has_key(key):
            self.alist.remove(key)
        elif len(self.dict) ==self.capacity:
            oldest_key=self.alist.pop() #从尾部pop
            self.dict.pop(oldest_key)
        
        self.dict[key]=value
        self.alist.insert(0,key) #插入头部
        
    
def test():
    c=LRUCache2(5)
    for i in range(5,10):
        c.set(i,10*i)
    
    print(c.dict,c.dict.keys())
    
    c.get(5)
    c.get(7)
    print(c.dict,c.dict.keys())
       
    c.set(10,100)
    print(c.dict,c.dict.keys())
    
    c.set(9,44)
    print(c.dict,c.dict.keys())
'''
(OrderedDict([(5, 50), (6, 60), (7, 70), (8, 80), (9, 90)]), [5, 6, 7, 8, 9])
(OrderedDict([(6, 60), (8, 80), (9, 90), (5, 50), (7, 70)]), [6, 8, 9, 5, 7])
(OrderedDict([(8, 80), (9, 90), (5, 50), (7, 70), (10, 100)]), [8, 9, 5, 7, 10])
(OrderedDict([(8, 80), (5, 50), (7, 70), (10, 100), (9, 44)]), [8, 5, 7, 10, 9])
'''
        


def test2():
    c=LRUCache2(5)
    for i in range(5,10):
        c.set(i,10*i)
    
    print(c.alist)
    
    c.get(5)
    c.get(7)
    print(c.alist)
       
    c.set(10,100)
    print(c.alist)
    
    c.set(9,44)
    print(c.alist)
    
test2()

