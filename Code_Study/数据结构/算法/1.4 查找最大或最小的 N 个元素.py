"""
    从一个集合或序列中获得最大或者最小的 N 个元素列表？
"""


import heapq


nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(2,nums))


# 两个函数都能接受一个关键字参数，用于更复杂的数据结构中：
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3,portfolio,key=lambda s:s['price'])   # 以 price 的值进行比较。
expensive = heapq.nlargest(1,portfolio,key=lambda s:s['price'])
print(cheap,expensive)