# def my_decorator(func):
#     def wrapper():
#         print("在原函数之前执行")
#         func()
#         print("在原函数之后执行")
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print("Hello!")
#
# say_hello()

# def outer(msg):
#     def inner():
#         print(msg)  # inner 记住了外层函数的变量 msg
#     return inner
#
# func = outer("Hello Closure!")
# func()  # 输出: Hello Closure!







# def log_decorator(func):
#     def wrapper(*args, **kwargs):  # 接受任意参数
#         print(f"准备执行函数：{func.__name__}")
#         result = func(*args, **kwargs)  # 执行原函数，并返回结果
#         print("执行完毕")
#         return result
#     return wrapper
#
# @log_decorator
# def add(a, b):
#     return a + b
#
# print(add(2, 3))

def fun_1(f):
    def fun_2(m,n):
        a = f(m,n)
        return a
    return fun_2
@fun_1
def max(m,n):
    if m>=n:
        return m
    else:
        return n

print(max(100,-200))

#####至此，装饰器应该算是学会了


# def my_decorator(func):  # func 是要装饰的函数
#     def wrapper():       # 这个函数会包裹原函数
#         print("装饰器：函数执行前做的事")
#         func()           # 执行原函数
#         print("装饰器：函数执行后做的事")
#     return wrapper       # 返回包装后的函数
# 第2步：使用装饰器
#
# PYTHON
# @my_decorator  # 把 say_hello 用 my_decorator 装饰
# def say_hello():
#     print("Hello!")
#
# say_hello()  # 调用被装饰后的函数
# 输出：
#
# TEXT
# 装饰器：函数执行前做的事
# Hello!
# 装饰器：函数执行后做的事