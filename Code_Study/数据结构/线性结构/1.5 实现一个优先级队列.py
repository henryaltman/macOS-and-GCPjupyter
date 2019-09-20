import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self,name):
        self.name = name
    def __repr__(self):     # 重构__repr__
        return 'Item({!r})'.format(self.name)


# 打印类对象并不是很友好，显示的是对象的内存地址,
# 重构__repr__方法后，不管直接输出对象还是通过print打印的信息都按我们__repr__方法中定义的格式进行显示了
# 重构__str__,直接输出对象ts时并没有按我们__str__方法中定义的格式进行输出，而用print输出的信息却改变了

# 如果你想在多个线程中使用同一个队列，那么你需要增加适当的锁和信号量机制。 可以查看 12.3 小节的例子演示是怎样做的。