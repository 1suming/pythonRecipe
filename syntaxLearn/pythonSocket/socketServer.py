#coding=utf-8
import socket
import sys
import time
import Queue
import threading

host='localhost'
port=8000
#创建socket对象
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定一个特定地址，端口
try:
    s.bind((host,port))
except Exception as e:
    print 'Bind failed:%s' %(str(e))
    sys.exit()
print 'socket bind complete'

#监听连接
s.listen(10)##最大连接数10
#创建连接队列
queue=Queue.Queue()

#创建线程
class TaskThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
        while 1:
            t=queue.get()
            t.send("welcome .....")
            #接受数据
            client_data=t.recv(1024)
            t.sendall(client_data)
            #释放资源
            #t.close()
    
    
#接受连接
while 1:
    #将连接放入队列
    conn,addr=s.accept()
    print 'Connected from %s:%s' %(addr[0],str(addr[1]))
    queue.put(conn)
    
    #生成线程池
    th=TaskThread()
    th.setDaemon(True)
    th.start()
    
    queue.join()
s.close()


    
