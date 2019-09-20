"""
    你的程序中有多个线程，你需要在这些线程之间安全地交换信息或数据
"""

# 从一个线程向另一个线程发送数据最安全的方式可能就是使用 queue 库中的队列

from queue import Queue
from threading import Thread

# A thread that produces data
def producer(out_q):
    while 1:
        out_q.put(data)   # 线程通过使用 put() 操作来向队列中添加元素

# A thread that consumes data
def consumer(in_q):
    while 1:
        data = in_q.get   # 线程通过使用 get() 操作来向队列中删除元素

q = Queue()     # 创建一个被多个线程共享的 Queue 对象
# 这些线程通过使用 put() 和 get() 操作来向队列中添加或者删除元素
# Queue 对象已经包含了必要的锁
t1 = Thread(target=consumer,args=(q,))
t2 = Thread(target=producer,args=(q,))
t1.start()
t2.start()

# 关闭会有一些麻烦