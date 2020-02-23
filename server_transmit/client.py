# server_transmit 客户端程序

import socket

HOST = '192.168.50.2'
PORT = 1201
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    data_recv = s.recv(1024).decode('utf-8')
    if data_recv == 'exit':
        print('Connection closed.')
        s.close()
        break
    else:
        print('Received:', data_recv)
    data_to_send = input('Send:')
    s.send(data_to_send.encode('utf-8'))


