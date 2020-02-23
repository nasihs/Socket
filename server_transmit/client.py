# server_transmit 客户端程序

import socket

HOST = '49.235.15.235'
PORT = 1201
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    data_recv = s.recv(1024).decode('utf-8')
    if data_recv == 'exit':
        print('服务器关闭了连接'）
        s.close()
        break
    else:
        print(data_recv)
    data_to_send = input('输入消息：')
    s.send(data_to_send)


