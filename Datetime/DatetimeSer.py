#!/usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('Waiting for connection....')
    tcpCliSock,addr = tcpSerSock.accept()
    print('Conected from:',addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break

        dateall = data + '    '.encode()+ ctime().encode()
        tcpCliSock.sendall(dateall)
    tcpCliSock.close()
tcpSerSock.close()
