"""
    为了对字典值执行计算操作，通常需要使用 zip() 函数先将键和值反转过来
"""

# 下面是查找最小和最大股票价格和股票值的代码：

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(),prices.keys()))
# min_price is (10.75, 'FB')

max_price = max(zip(prices.values(),prices.keys()))
# max_price is (612.78, 'AAPL')

prices_sorted = sorted(zip(prices.values(), prices.keys()))
# prices_sorted is [(10.75, 'FB'), (37.2, 'HPQ'),
#                   (45.23, 'ACME'), (205.55, 'IBM'),
#                   (612.78, 'AAPL')]