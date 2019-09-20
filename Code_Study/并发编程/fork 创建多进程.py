import os
from time import sleep

print('==========')
a = 1

pid = os.fork()  # 返回值赋值给 pid

if pid < 0:     # 返回值为负数，创建失败
    print('Can not create a new process.')
elif pid == 0:  # 返回值为零，在原有进程中返回新进程的 PID，在新进程中返回 0
    os._exit(1)
    sleep(1)
    print('New')
else:       # 返回值为正数，
    sleep(3)
    print('Old')

print("Fork test end.")