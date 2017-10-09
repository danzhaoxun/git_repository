#!/usr/bin/env python

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    date = input('> ')
    if not date:
        break
    tcpCliSock.sendall(date.encode())
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data)
tcpCliSock.close()