# Queue测试  q.get后队列是否为空

from queue import Queue
import threading
# from time import sleep

q1 = Queue()
q2 = Queue()
# q2 = Queue()
i = 1


def client1(q1, q2):
    data = 'This is a message from client 1.'
    q1.put(data)
    data = 'This is a message from client 1.'
    q1.put(data)
    data = 'This is a message from client 1.'
    q1.put(data)


def client2(q1, q2):
    while True:
        if not q1.empty():
            print(q1.get(), q1.empty())
        else:
            print(q1.empty())
            break
        #print(data, i)
    # print('Queue is empty')


t1 = threading.Thread(target=client1, args=(q1, q2,))
t2 = threading.Thread(target=client2, args=(q1, q2,))
t1.start()
# sleep(5)
t2.start()
t1.join()
t2.join()
print('Finished')
