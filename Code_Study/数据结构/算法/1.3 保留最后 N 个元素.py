"""
    怎样只保留最后有限几个元素的历史记录？
"""

# 保留有限历史记录正是 collections.deque 大显身手的时候。

from collections import deque


# 在写查询元素的代码时，通常会使用包含 yield 表达式的生成器函数
def search(lines,pattern,history=5):
    previous_line = deque(maxlen=history)       # 使用 deque(maxlen=N) 构造函数会新建一个固定大小的队列。当新的元素加入并且这个队列已满的时候， 最老的元素会自动被移除掉。
    for line in lines:
        if pattern in line:
            yield line,previous_line
        previous_line.append(line)


# deque 类可以被用在任何你只需要一个简单队列数据结构的场合

# 在队列两端插入或删除元素时间复杂度都是 O(1) ，区别于列表，在列表的开头插入或删除元素的时间复杂度为 O(N) 。