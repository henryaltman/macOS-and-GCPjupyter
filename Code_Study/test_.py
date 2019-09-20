import sys
import inspect


def f(a=1, b=2, c=3):
  print(locals())  # 在函数内获取


f()
print('1--------------------')
#使用inspect模块，简单方便

# inspect.getargspec(f)
# inspect.signature(f)
# inspect.getfullargspec(f)
print('2--------------------')
#使用f的内置方法

#获取默认值,如果参数名没有默认值则不在其中：
print(f.__defaults__)
print('3--------------------')
#使用__code__

#总参数个数
print(f.__code__.co_argcount)
print('4--------------------')
#总参数名
print(f.__code__.co_varnames)
print('5--------------------')

# 获取当前函数名称


def my_name():
    print '1', sys._getframe().f_code.co_name
    print '2', inspect.stack()[0][3]


def get_current_function_name():
    print '5', sys._getframe().f_code.co_name
    return inspect.stack()[1][3]


class MyClass:
    def function_one(self):
        print '3', inspect.stack()[0][3]
        print '4', sys._getframe().f_code.co_name
        print "6 %s.%s invoked" % (self.__class__.__name__, get_current_function_name())
