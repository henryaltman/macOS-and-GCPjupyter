"""
    为需要并发执行的代码创建/销毁线程
"""

# threading 库可以在单独的线程中执行任何的在 Python 中可以调用的(callable)对象。
# 你可以创建一个 Thread 对象并将你要执行的对象以 target 参数的形式提供给该对象。

import sys
# Code to execute in an independent thread
import time
def countdown(n):
    while n > 0:
        print('T-minus',n)
        n -= 1
        time.sleep(1)


# Create and launch a thread
from threading import Thread
t = Thread(target=countdown,args=(10,))     # 当你新建好一个线程对象后，该对象并不会立即执行
t.start()   # 当你调用 start() 方法时，它会调用你传递进来的函数，并把你传递进来的参数传递给该函数

# Python中的线程会在一个单独的系统级线程中执行（比如说一个 POSIX 线程或者一个 Windows 线程）
# 这些线程将由操作系统来全权管理。
# 线程一旦启动，将独立执行直到目标函数返回。

# 你可以查询一个线程对象的状态，看它是否还在执行：
if t.is_alive():
    print("Still running")
else:
    print('Completed')

# 你也可以将一个线程加入到当前线程，并等待它终止(cannot join thread before it is started)：
t.join()    # 作用是主线程阻塞，等待子线程结束
# join方法有一个参数是timeout，即如果主线程等待timeout，子线程还没有结束，则主线程强制结束子线程。
# 如果同时有N个子线程join(timeout），那么实际上主线程会等待的超时时间最长为 N ＊ timeout
# 因为每个子线程的超时开始时刻是上一个子线程超时结束的时刻。

# sys.exit()      # Python解释器直到所有线程都终止前仍保持运行。这样的退出不影响t 线程

# 对于需要长时间运行的线程或者需要一直运行的后台任务，你应当考虑使用后台线程。
t1 = Thread(target=countdown,args=(10,),daemon=True)    # 这些线程会在主线程终止时自动销毁。
t1.start()    # daemon=True,主线程执行完毕后自动退出，不会等待子线程的执行结果。


# 由于全局解释锁（GIL）的原因，Python 的线程被限制到同一时刻只允许一个线程执行这样一个执行模型。
# 所以，Python 的线程更适用于处理I/O和其他需要并发执行的阻塞操作（比如等待I/O、等待从数据库获取数据等等）
# 而不是需要多处理器并行的计算密集型任务。

