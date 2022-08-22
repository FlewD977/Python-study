# 复用
"""
格式：
def 函数名([参数，...]):
    代码
参数：
1.无参数：def function():

2.有参数：def function ([参数]):

代码：封装重复内容

调用函数：
function    不加括号代表的是查找对应地址
function()  调用执行空间内的代码

debug时需要在函数内部也加一个断点才会debug进去

默认值参数：在定义函数的是时候，有一个或者多个参数已经赋值
def （参数一，参数二=xx）
调用特点：有默认值的参数可以不传参

关键字传输赋值：给特定的关键字参数传参
def xxx（参数一，参数二=xx）
xxx（参数二=123）

"""

# choice() 方法返回一个列表，元组或字符串的随机项。
import random


def gennum(tmp):
    s = 'qwertyuiopzxcvbnmasdfhgjkl1234567890'
    code = ''
    for i in range(tmp):
        r = random.choice(s)
        code += r
    print(code)


# 调用该函数
gennum(5)

"""
定义一个logo函数：
admin 1234
输入用户名和密码，验证是否正确
"""


def logo():
    username = input('用户名：')
    password = input('密码：')
    if username == 'admin' and password == '1234':
        print('登录成功')
    else:
        print('登录失败')


# logo()


# 函数传多个参数
# isinstance 判断类型是否符合
def logo_1(a, b):
    if isinstance(a, int) and isinstance(b, int):
        s = a + b
        print(s)


logo_1(1, 3)

# 可变参数
"""
传参时函数的接收变量可变
*args
**kwargs

装包和拆包
函数装包：
def 函数（*xxx）：----》此时会出现装包
    pass
函数（1，2，3，4）

函数拆包：
调用的时候 函数（*list）
"""
# *args
a, *b, c = 1, 2, 3, 4, 5, 6, 7


# python底层加*号的变量会默认再赋值的情况下 放入一个列表中
# print(a)    1
# print(b)    [2, 3, 4, 5, 6]
# print(c)    7


def a_b(*a):
    print(a)


# a_b(1, 2, 3, 4, 5, 6, 7, 89)        1 2 3 4 5 6 7 89
# a_b(1, 2, )                         1 2


def a_c1(*a):
    s = 0
    for i in a:
        s += i
    print(s)


# a_c1(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)     55

# 若传参时传入的是一个列表则需要在调用函数的时候加*
ran_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# a_c1(ran_list)      TypeError: unsupported operand type(s) for +=: 'int' and 'list'
# a_c1(*ran_list)     45


# **kwargs
"""
只能传键值对的参数
"""


def shiw_book(**kwargs):
    print(kwargs)


# print(kwargs)       {}

shiw_book(bookname='西游记', author='吴承恩', prince=5)
# {'bookname': '西游记', 'author': '吴承恩'}

book = {'bookname': 'flkew', 'author': 'hello'}
shiw_book(**book)


# {'bookname': 'flkew', 'author': 'hello'}

# 多个可变参数
def show_book(*arg, **kwarg):
    print(arg)
    print(kwarg)


# 函数的返回值
"""
使用return 返回参数
"""


def num(*arg):
    conut1 = 0
    for i in arg:
        conut1 += i
    return conut1


c1 = num(1, 3, 4)
x = 100
x += c1
print(x)


# 返回多个参数
def get_maxmin(numbers):
    for i in range(0, len(numbers) - 1):
        for j in range(0, len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[i], numbers[j + 1] = numbers[j + 1], numbers[j]
    min = numbers[0]
    mix = numbers[-1]
    return min, mix


numbers = [10, 20, 51, 2, 3, 4, 5, 2, 1, 87, 52, 1]
result = get_maxmin(numbers)
print(result)

# 不可变、可变的类型
# 内容发生改变时地址发生该改变
# 内容发生改变时地址不发生该改变
"""
global关键字的添加
只有不可变的类型才需要添加global
可变的类型不需要添加global

不可变类型：
list,dict,set
可变类型
int,str,float,tuple，bool
"""

# 全局变量和局部变量

m = 100

# def nu_1():
#     nonlocal m  表示引用外侧的局部变量m
#     m -= 10  # 当使用m=m-10 函数会在自身寻找m
#     print(m)  # 100 函数会使用全局变量 但是不能更改


# 闭包
""""
1.嵌套函数
2.内部函数使用了外部函数的变量
3.返回值是内部函数
主要用在装饰器上
"""


# 将内部函数返回出去 在外部随时调用
def outer(n):
    a = 10

    def inner():
        b = a + n
        print("内部函数", b)

    return inner


result1 = outer(5)  # 接收内部函数地址
print(result1)
# <function outer.<locals>.inner at 0x000001D0D8F4E700>


result1()  # 内部函数地址加（）是调用
# 内部函数 15


# 递归函数
"""
一个函数在内部不调用其他函数，而是自己本身则 这个函数就是递归函数
遵循：
1.必须要有出口
2.每次递归向出口靠近
"""


def test(i):
    print('test---------->')
    if i == 10:
        print('10')
    else:
        print(i)
        i += 1

        test(i)


test(0)


# 累加和
def test_sum(i):
    if i == 10:
        return 10
    else:
        return i + test_sum(i + 1)


rr = test_sum(0)
print(rr)

# 匿名函数
"""
使用lambda关键字创建小型匿名函数
这种函数省略了def声明函数的标准步骤
表示函数非常简单 不用def来声明

格式：
lambda 参数列表：运算表达式

使用场景：
在函数中作为参数使用
"""
hh = lambda i: i + 1
hh(2)  # 调用函数


def funnn1(a, f):
    print('--------------------->')
    rr = f(a)
    print(rr)


funnn1(8, lambda x: x ** 2)

# 高阶函数
"""
一个函数的参数是另一个函数，称为高阶函数
系统高阶函数：
max min sorted 
"""
