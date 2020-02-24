"""服务端转发 ver 0.1
客户端每发送一次才能从服务端接收一次
"""


import socket
import threading
from queue import Queue


def deal_client1(conn, addr, q1, q2):
    conn.send(b'Hello, I am server')
    while True:
        # 接收来自Client1的消息并发送给线程：deal_client2
        # 收到exit后通知客户端断开连接
        data_to_send = conn.recv(1024)
        if data_to_send.decode('utf-8') == 'exit':
            q1.put(b'exit')
            conn.send(b'exit')
            conn.close()
            break
        else:
            q1.put(data_to_send)
        # 接收来自Client2的消息并发送给Client1
        if not q2.empty():
            data_recv = q2.get()
            conn.send(('Message from Client2: %s ' % data_recv.decode('utf-8')).encode('utf-8'))
        else:
            continue


def deal_client2(conn, addr, q1, q2):
    conn.send(b'Hello, I am server')
    while True:
        # 接收来自Client2的消息并发送给线程：deal_client1
        data_to_send = conn.recv(1024)
        if data_to_send.decode('utf-8') == 'exit':
            q2.put(b'exit')
            conn.send(b'exit')
            conn.close()
            break
        else:
            q2.put(data_to_send)
        # 接收来自Client2的消息并发送给Client2
        if not q1.empty():
            data_recv = q1.get()
            conn.send(('Message from Client2: %s ' % data_recv.decode('utf-8')).encode('utf-8'))
        else:
            continue


def main():
    HOST = ''
    PORT = 1201
    q1 = Queue()
    q2 = Queue()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen(5)
        print('Waiting for Client1...')
        conn1, addr1 = s.accept()
        conn1.send(b'Connected.')
        print('Accept Client1 from %s : %s..' % addr1)
        print('Waiting for Client2...')
        conn2, addr2 = s.accept()
        conn2.send(b'Connected.')
        print('Accept Client2 from %s : %s..' % addr2)
        # 开启进程处理Client消息
        t1 = threading.Thread(target=deal_client1, args=(conn1, addr1, q1, q2,))
        t2 = threading.Thread(target=deal_client2, args=(conn2, addr2, q1, q2,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    print('Done.')


if __name__ == '__main__':
    main()
