# 服务端转发程序
# data = self.socket.recv(1024, socket.MSG_WAITALL)  接收到指定长度才返回

from __future__ import print_function
import socket
import threading
# import time
from queue import Queue

HOST = ''
PORT = 1201


def deal_client1(sock, addr, q1, q2):
    while True:
        # 接收来自Client1的消息并发送给线程：deal_client2
        data_to_send = sock.recv(1024)
        if data_to_send.decode('utf-8') == 'exit':
            q1.put(b'exit')
            sock.close()
            break
        else:
            q1.put(data_to_send)
        # 接收来自Client2的消息并发送给Client1
        if not q2.empty():
            data_recv = q2.get()
            sock.send(('Message from Client2: %s ' % data_recv.decode('utf-8')).encode('utf-8'))
        else:
            continue


def deal_client2(sock, addr, q1, q2):
    while True:
        # 接收来自Client2的消息并发送给线程：deal_client1
        data_to_send = sock.recv(1024)
        if data_to_send.decode('utf-8') == 'exit':
            q2.put(b'exit')
            sock.close()
            break
        else:
            q2.put(data_to_send)
        # 接收来自Client2的消息并发送给Client2
        if not q1.empty():
            data_recv = q1.get()
            sock.send(('Message from Client2: %s ' % data_recv.decode('utf-8')).encode('utf-8'))
        else:
            continue


def main():
    q1 = Queue()
    q2 = Queue()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(5)
        print('Waiting for Client1...')
        sock1, addr1 = s.accept()
        print('Accept Client1 from %s : %s..' % addr1)
        print('Waiting for Client2...')
        sock2, addr2 = s.accept()
        print('Accept Client2 from %s : %s..' % addr2)

        t1 = threading.Thread(target=deal_client1, args=(sock1, addr1, q1, q2,))
        t2 = threading.Thread(target=deal_client2, args=(sock2, addr2, q1, q2,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    print('Done.')


if __name__ == '__main__':
    main()
