"""
    你有一些C函数已经被编译到共享库或DLL中。
    你希望可以使用纯Python代码调用这些函数， 而不用编写额外的C代码或使用第三方扩展工具。
"""

import ctypes
import os


# 假设你有一个共享库名字叫 libsample.so ，里面的内容就是15章介绍部分那样。
# 另外还假设这个 libsample.so 文件被放置到位于 sample.py 文件相同的目录中了。
# 定位 .so 文件
file_ = 'libsample.so'
path_ = os.path.join(*(os.path.split(__file__)[:-1] + (file_,)))
mod_ = ctypes.cdll.LoadLibrary(path_)

# int gcd(int, int)
gcd = mod_.gcd
gcd.argtypes = (ctypes.c_int, ctypes.c_int)
gcd.restype = ctypes.c_int
