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

    def push(self, element):
        self.top = Node(element, self.top)  # 改变局部状态以反映质能的变化   101

    def pop(self):  # 查
        if self.top is None:    # 分情况，反面情况优先
            raise StackError
        value = self.top.data   # 变量作为情况的保存   010
        self.top = self.top.next  # 改变局部状态以反映质能的变化   101
        return value    # 变量作为要反映出去的信息  011

    def top(self):  # 查
        if self.top is None:    # 分情况，反面情况优先
            raise StackError
        return self.top.data    # 变量作为要反映出去的信息  011


