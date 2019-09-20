"""
    实现一个键对应多个值的字典（也叫 multidict）？
    这一小节所讨论的问题跟数据处理中的记录归类问题有大的关联。
"""

# 你可以很方便的使用 collections 模块中的 defaultdict 来构造这样的字典。
from collections import defaultdict


# defaultdict 的一个特征是它会自动初始化每个 key 刚开始对应的值，所以你只需要关注添加元素操作了。

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)
# defaultdict(<class 'list'>, {'a': [1, 2], 'b': [4]})

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d)
# defaultdict(<class 'set'>, {'a': {1, 2}, 'b': {4}})