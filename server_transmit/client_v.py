"""客户端TCP程序 ver 0.3
实现同时收发
"""


import socket
from threading import Thread
import sys

HOST = '49.235.15.235'
PORT = 1201
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpCliSock.connect(ADDR)


def sendData():
    while True:
        data = input('')
        if not data:
            continue
        tcpCliSock.send(data.encode('utf-8'))


Thread(target=sendData).start()
while True:
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        sys.exit(0)
    print(data.decode('utf-8'))

tcpCliSock.close()
