# Queue测试  q.get后队列是否为空

from queue import Queue
import threading

q = Queue()
i = 1


def client1(q):
    data = 'This is a message from client 1.'
    q.put(data)
    data = 'This is a message from client 2.'
    q.put(data)


def client2(q):
    data = q.get()
    print(data, 1)
    data = q.get()
    print(data, 2)



t1 = threading.Thread(target=client1, args=(q,))
t2 = threading.Thread(target=client2, args=(q,))
t1.start()
t2.start()
t1.join()
t2.join()
print('Finished')