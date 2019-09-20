from threading import Thread,Event
from threading import Lock

e = Event()

gate_num = 0
gate_later = 0

target2 = 'ABCDEFGHIJKLNOPQRSTUVWXYZ'


def print_num(num):
    target1 = list(range(1, 53))
    for i in target1:
        lock.acquire()
        print(i.po(0),end='')
        print(i.pop(0),end='')
        lock.release()


def print_later():

    for i in target2:
        lock2.acquire()
        print(i)
        lock2.release()


lock = Lock()
lock2 = Lock()

t1 = Thread(target=print_num)
t2 = Thread(target=print_later)

t1.start()

t2.start()
