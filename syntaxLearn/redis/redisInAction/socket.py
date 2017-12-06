import socket

import subprocess

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket.bind(('127.0.0.1',8001))

socket.listen(5)

while True:

	connection,addr = socket.accept()

	buf=connection.recv(1024)

	d=subprocess.Popen('ls -l /tmp', stdout=subprocess.PIPE, shell=True)

	connection.send("You give me" + buf+"\n")

	connection.send("".join(d.stdout.readlines()))

	connection.close()
