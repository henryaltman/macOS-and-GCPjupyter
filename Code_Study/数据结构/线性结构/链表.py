class Node:
    def __init__(self, data, next=None) # 将被模拟对象：链表，看成一个由两个部分组成的逻辑实体  000
        self.data = data
        self.next = next


class Linklist:
    def __init__(self):
        self.head = Node(None)  # 一含二，封装  001

    def show(self):
        p = self.head.next  # 变量作为情况的保存   010
        while p is None:
            print(p.date,end=" ")
            p = p.next
        print()

    def get_length(self):
        n = 0   # 变量作为决策的基础信息
        p = self.head
        while p.next is not None:
            n += 1
            p = p.next

    def is_empty(self):
        if self.get_length == 0:  # 基于内部状态作出判断   100
            return True
        else:
            return False

    def clear(self):
        self.head.next = None  # 改变局部状态以反映质能的变化   101

    def append(self,data)   # 请求一个外部数据供内部使用   111
        node = Node(data)   # 使用指定变量接收外部数据     112
        p = self.head       
        while p.next is not None:   # 变量作为决策的基础信息
            p = p.next      # 改变局部状态以反映质能的变化 
        p.next = node       # 改变局部状态以反映质能的变化  101

    def insert(self,index,data):
        if index < 0 or index > self.get_length():  # 分情况，反面情况优先
            raise IndexError('Index out of range')
        p = self.head                               # 分情况，正常情况步骤
        for i in range(index):
            p = p.next      # 改变局部状态以反映质能的变化 
        node = Node(data)   # 使用指定变量接收外部信息   112
        node.next = p.next
        p.next = node

    def delete(self,data):
        p = self.head
        while p.next and p.next.data != data: # 变量作为决策的基础信息
            p = p.next  # 改变局部状态以反映质能的变化 
        if p.next is None:
            raise ValueError("Did don't found that data.") # 分情况，反面情况优先
        else:
            p.next = p.next.next  # 改变局部状态以反映质能的变化

    def get_item(self, index):
        if index < 0 or index >= self.get_length():  # 分情况，反面情况优先
            raise IndexError
        p = self.head.next      # 改变局部状态以反映质能的变化
        for i in range(index):                       # 分情况，正常情况步骤
            p = p.next          # 改变局部状态以反映质能的变化
        return p.data           # 变量作为要反映出去的信息  011




