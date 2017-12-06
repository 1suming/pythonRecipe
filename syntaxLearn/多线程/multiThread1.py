#coding=utf-8
import threading,time
class MyThread(threading.Thread):
    def __init__(self,threadName):
        threading.Thread.__init__(self,name=threadName)
    def run(self):
        for i in xrange(1000):
            print self.getName,i
            time.sleep(1)
            
'''
my=MyThread("test")
my.start()
my2=MyThread("test2")
my2.start()
'''
t1=MyThread("t1")
print t1.getName(),t1.isDaemon()
t1.setDaemon(True)
print t1.getName(),t1.isDaemon()
t1.start()
print 'main thread exit'