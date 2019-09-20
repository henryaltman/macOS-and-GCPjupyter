"""
    逆波兰表达式
"""


class StackError(Exception):
    pass

class Node:
    def __init__(self, data, next=None):  # 将被模拟对象：链表：栈，看成一个由两个部分组成的逻辑实体  000
        self.data = data
        self.next = next

class LStack:
    def __init__(self):
        self.top = None    # 添加被模拟对象：链表：栈的限制条件

    def is_empty(self):
        return self.top is None

    def push(self, element):    # 增
        self.top = Node(element, self.top)  # 改变局部状态以反映质能的变化   101

    def pop(self):  # 查&删
        if self.top is None:    # 分情况，反面情况优先
            raise StackError
        value = self.top.data   # 变量作为情况的保存   010
        self.top = self.top.next  # 改变局部状态以反映质能的变化   101
        return value    # 变量作为要反映出去的信息  011

    def top(self):  # 查
        if self.top is None:    # 分情况，反面情况优先
            raise StackError
        return self.top.data    # 变量作为要反映出去的信息  011


ls = LStack()

while 1:
    expression = input()
    temp = expression.split(' ')
    for i in temp:
        if i not in ['+', '-', 'p']:      # 分情况，反面情况优先
            ls.push(float(i))
        elif i == '+':
            x = ls.pop()
            y = ls.pop()
            ls.push(x + y)     # 改变局部状态以反映质能的变化   101
        elif i == '-':
            x = ls.pop()
            y = ls.pop()
            ls.push(- x + y)
        elif i == 'p':
            print(ls.top())
