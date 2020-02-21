import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    for data in [b'Michael', b'Tracy', b'Sarah']:
        # 发送数据:
        # s.sendto(data, ('192.168.50.3', 7777))
        s.sendto(data, ('223.104.211.188', 7777))
        # 接收数据:
        print(s.recv(1024).decode('utf-8'))

s.close()
