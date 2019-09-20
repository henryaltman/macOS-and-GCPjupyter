"""
    假定你要从一个记录（比如文件或其他类似格式）中的某些固定位置提取字段：
"""


record = '....................100 .......513.25 ..........'
# 这样命名切片: 使得你的代码更加清晰可读。
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])

# slice() 函数创建了一个切片对象。所有使用切片的地方都可以使用切片对象。
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[2:4])
# [2, 3]
print(items[a])
# [2, 3]


# 如果你有一个切片对象a，你可以分别调用它的 a.start , a.stop , a.step 属性来获取更多的信息