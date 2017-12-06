#coding=utf-8
import socket
import time
import sys

#设置连接请求30s超时
socket.setdefaulttimeout(30)

#ipv4协议、字节流（tcp协议）
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as  e:
    print 'Socket  error:%s' %(str(e))
    sys.exit()
print 'Socket created'

#host='www.baidu.com'
host='localhost'
port=8000
try:
    remote_ip=socket.gethostbyname(host)
except socket.gaierror as e:
    print 'get %s ip error %s' % (host,str(e))
    sys.exit()
print 'ip address of %s is %s' % (host,remote_ip)

#连接服务器(SOCK_STREAM/TCP 套接字才有“连接”的概念,一些 Socket 如 UDP、ICMP 和 ARP 没有“连接”的概念)
try:
    s.connect((remote_ip,port))
except Exception as e:
    print 'scoket conncet %s:%s failed,error: %' % (host,port,str(e))
    
#发送数据，根据http1.1协议
'''请求消息结构如下:
请求方法 路径 http版本\r\n -请求行
请求头域1:值 \r\n
请求头域2:值\r\n
....以上均为请求头
一个空行\r\n -头与主体间的空行
请求主体
'''
msg="GET /php/phpSyntax/test.php HTTP/1.1\r\n"
#请求header(HTTP/1.1请求必须包含主机头域，否则系统会以400状态码返回)
msg+="Host: localhost\r\n"  
#空行
msg+='\r\n'
#请求body（由于这里是GET请求，body没有)

try:
     #这里也可用send()方法：不同在于sendall在返回前会尝试发送所有数据
    #并且成功时返回是None，而send()则返回发送的字节数量。失败时都抛出异常。
    s.sendall(msg)
except Exception as e:
    print 'send failed'
    sys.exit()
print 'Msg Send successfully!'

def recv_timeout(the_socket,timeout=2):
    #make socket non blocking
    the_socket.setblocking(0)
    #total data partwise in an array
    total_data=[]
    data=''
    
    #beginning time
    begin=time.time()
    while 1:
        #if you get some data ,then break after timeout
        if total_data and time.time()-begin >timeout:
            break;
        #if you got no data at all,wait a little longer,twice the timemoout
        elif time.time()-begin > timeout*2  :
            break;
        #recv something
        try:
            data=the_socket.recv(8192)
            if data:
                total_data.append(data)
                #change the beginning time 
                begin=time.time()
            else:
                #sleep for sometime to indictate a gap
                time.sleep(0.1)
        except:
            pass
    
    #join all parts to make final string
    return ''.join(total_data)
            
#获取服务器返回的数据
#response=s.recv(4096,s.MSG_WAITALL)#这里还可用recvfrom()、recv_into()等等
response=recv_timeout(s)
print response
s.close()


    