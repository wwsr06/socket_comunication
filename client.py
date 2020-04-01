# -*- coding:utf-8 -*-
import socket
import time

client = socket.socket()


#client.connect(('103.100.209.164',8888))
client.connect(('127.0.0.1',8888))


while True:
    data = raw_input('>>>:')
    if data == "":
    	data = "NULL"
    
    client.send(data.encode('utf-8'))


    data_recv = client.recv(1024)
    print(data_recv.decode())

client.close()