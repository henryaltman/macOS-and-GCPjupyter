"""
    有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给 N 个变量？
"""


# 序列、可迭代对象
p = (1,2)
x,y = p


data = ['AC',50,2.3,(12,6,12)]
name, shares,price,(year,mon,day) = data


# 这种解压赋值可以用在任何可迭代对象上面
s = 'Hello'
a,b,c,d,e = s


"""
    1.2 解压可迭代对象赋值给多个变量
"""

# 一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError
# 你想统计下家庭作业的平均成绩，但是排除掉最高和最低分数。
grades = [1,20,34,56,23,78,100,99,100]
first, *middle,last = sorted(grades)
print(*middle)

# 你现在有一些用户的记录列表，每条记录包含一个名字、邮件，接着就是不确定数量的电话号码。 你可以像下面这样分解这些记录：
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name_, email, *phone_numbers = record     # 解压出的 *phone_numbers 变量永远都是列表类型


# 你有一个公司前 8 个月销售数据的序列， 但是你想看下最近一个月数据和前面 7 个月的平均值的对比。你可以这样做：
sales_record = [112,334,123,535,6465,4657,4788,123415]
*trailing_sales, current_sales = sales_record
print(current_sales)   # 123415


# 星号表达式在迭代元素为可变长（不定长）元组的序列时是很有用的。 比如，下面是一个带有标签的元组序列：
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x,y):
    print('foo',x,y)

def do_bar(x,y):
    print('bar',s)

for tag,*args in record:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


# 星号解压语法在字符串操作的时候也会很有用，比如字符串的分割。
s_line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'

uname,*fields,homedir,sh = s_line.split(":")
print(uname)        # nobody
print(homedir)      # /var/empty
print(sh)           # /usr/bin/false