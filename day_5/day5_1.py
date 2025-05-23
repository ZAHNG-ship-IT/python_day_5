####匿名函数lambda arguments: expression


from functools import reduce

numbers = [1, 2, 3, 4, 5]

# 使用 reduce() 和 lambda 函数计算乘积
product = reduce(lambda x, y: x * y, numbers)

print(product)  # 输出：120



#####匿名函数写法就是 表达式 = lambda 参数列表: 函数体  只有这一行代码