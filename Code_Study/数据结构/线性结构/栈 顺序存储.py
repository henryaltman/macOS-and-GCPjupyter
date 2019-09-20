class StackError(Exception):
    pass


class SStack:
    def __init__(self):       # 将被模拟对象：栈，看成一个由以个部分组成的逻辑实体 000
        self.elements = []    # 使用指定变量接收外部数据     112

    def is_empty(self):       # 有没有
        return self.elements == []   # 变量作为要反映出去的信息  011

    def push(self, elem):
        self.elements.append(elem)   # 改变局部状态以反映质能的变化

    def pop(self):
        if not self.elements:   # 分情况，反面情况优先
            raise StackError
        return self.elements.pop()  # 局部状态作为输出

    def show_top(self):
        if not self.elements:   # 分情况，反面情况优先
            raise StackError
        return self.elements[-1]    # 局部状态作为输出
