class QueueError(Exception):
    pass

class SQueue:
    def __init__(self):   # 将被模拟对象：队列，看成一个由另一个逻辑实体限制下的逻辑实体  001
        self.elements = []

    def is_empty(self):     # 查
        return self.elements == []

    def enqueue(self, elem):    # 增
        self.elements.append(elem)  # 改变局部状态以反映质能的变化

    def dequeue(self, elem):        # 查&删
        if not self.elements:       # 分情况，反面情况优先
            raise QueueError('Queue is empty')
        return self.elements.pop(0)  # 改变局部状态以反映质能的变化
