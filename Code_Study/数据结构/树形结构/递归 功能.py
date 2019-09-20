"""
    实现阶乘
"""
# 1,用循环
def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


# 1,用递归
def factorial_recursion(num):
    if num <= 1:     # 递归终止条件   分情况，反面情况优先
        return 1
    return factorial_recursion(num - 1) * num   # 每一层递归的外部环境都是类似的
