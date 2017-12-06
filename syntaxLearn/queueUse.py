#coding=utf-8
import Queue
q=Queue.Queue(5)
print q.empty()
for i in xrange(5):
    q.put(i)

while not q.empty():
    print q.get(),
    

