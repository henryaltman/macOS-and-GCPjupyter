class QueueError(Exception):
    pass

class Node:
    def __init__(self,data, next=None):
        self.data = data
        self.next = next

class LQueue:
    def __init__(self):     # 将被模拟对象：队列，看成一个由另一个逻辑实体限制下的逻辑实体  001
        self.front = self.rear = Node(None)   # 变量作为情况的保存*2   010

    def is_empty(self):
        return self.front == self.rear   # 基于内部状态作出判断   100

    def enqueue(self, elem):    # 增
        self.rear.next = Node(elem)
        self.rear = self.rear.next      # 改变局部状态以反映质能的变化

    def dequeue(self, elem):    # 查&删
        if self.front == self.rear:    # 分情况，反面情况优先
            raise QueueError('Queue is empty')
        self.front = self.front.next    # 改变局部状态以反映质能的变化
        return self.front.data 

