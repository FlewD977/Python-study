# 生成器 generator
"""
通过列表推导式可以直接创建list
但是收到内存限制，列表的容量是有限的，若创建一个很大的元素则会占用很大的空间
所以用到一种一边循环一边计算的机制，称为生成器
generator

得到生成器的方式：
1、通过列表推导式得到生成器
2、借助函数完成
3、
"""

new_list = [i * 3 for i in range(10)]
print(type(new_list))
# <class 'list'>
# [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

# 将[]换位（）则代表得到生成器
new_list_1 = (i * 3 for i in range(10))
print(type(new_list_1))
# <class 'generator'>

# 直接调用无法获得参数
print(new_list_1)
# <generator object <genexpr> at 0x000001BCF70CDEB0>

# 方法一 通过调用__next__() 每调用一次则会产生数据 避免消耗内存
print(new_list_1.__next__())
# 0
print(new_list_1.__next__())
# 3

# 方法二 next（生成器对象） builtins使用系统内置函数
print(next(new_list_1))
# 6

while True:
    try:
        e = next(new_list_1)
        print(e)
    except:  # 使用try except避免报错
        print("没有更多元素了")
        break
print('---------------------------')

# 方法二 借助函数完成
"""
1、定义一个函数,使用yield关键字
2、调用函数，接收嗲用的结果
3、得到的结果就是生成器
4、借助__next__() 得到元素
"""


# yield关键字
def funnc():
    n = 0
    while True:
        n += 1
        # print(n)
        yield n  # 函数中只要出现yield关键字代表当前函数变为生成器
        # 若不调用yield 就陷入死循环 类似return n +暂停


e1 = funnc()
print(e1)
# <generator object funnc at 0x000001CF10F25580>

# 调用生成器 只要执行这一步是才进入生成器内部
print(e1.__next__())


# 斐波那契数列
# 0 1 1 2 3 5 8 13
def fib(lens):
    a, b = 0, 1  # 第一个和第二个元素
    n = 0  # 控制元素个数

    while n < lens:
        # print(b)  # 打印第二个指
        yield b
        a, b = b, a + b  # 将a重新复制为b b累加值变成第三个值
        n += 1

    return '没有更多元素'  # 若条件不符合则会返回这个报错信息


g1 = fib(8)

print(g1.__next__())
# 1
print(g1.__next__())
# 1
print(g1.__next__())
# 2
print(g1.__next__())
# 3
print(g1.__next__())

# 5

print('---------------------')

# 生成器方法
"""
__next__():获取下一个元素
send（value）：向每次生成器调用中传值，第一次调用必须先传空值None
"""


def gen():
    i = 0
    while i < 5:
        temp = yield i  # return 0 +暂停 返回一个0 将函数暂停 直到遇到send
        print("temp:", temp)
        i += 1
    return '没有更多数据'


h1 = gen()

# print(h1.__next__())
# # 0
# # temp: None
# print(h1.__next__())
# # 1
# # temp: None
# print(h1.__next__())
# # 2

# send()
# 前面代码无屏蔽
# n1 = h1.send('hehe')
# print("n1:", n1)
# # temp: hehe
# # n1: 3
#
# n2 = h1.send('hhhhh')
# print("n2:", n2)
# # temp: hhhhh
# # n2: 4

# 前面代码屏蔽后
print(h1.send(None))

# send（）
# 将值传给生成器 yield拿到值
n3 = h1.send('nihao')
print(n3)
# 0
# temp: nihao
# 1
print('------------')

n4 = h1.send('flew')
print(n4)

# temp: flew
# 2


# 多线程协程
nums = 5


def f1(num):
    for i in range(num):
        print(f"正在搬转{i}")
        yield


def f2(num):
    for n in range(num):
        print(f"正在进行{n}")
        yield


g1 = f1(nums)
g2 = f2(nums)

# 达到交替执行
# while True:
#     try:
#         g1.__next__()
#         g2.__next__()
#     except:
#         pass
# g1.__next__()
# g2.__next__()


# 迭代器 Iterable
"""
是访问集合元素的一种方式，可以记住遍历的位置的对象
从集合第一个元素开始访问直至所有的访问完结束
只能前进不能后退
可以被next（）函数调用并不断返回下一个值的对象称为迭代器Iterable

1、生成器
2、列表 集合 字典 字符串
判断是否为可迭代对象
isinstance

可迭代对象不一定就是迭代器
iter()函数可以将可迭代对象变成迭代器

"""
from collections import Iterable

lis2 = [1, 2, 5, 4, 6]
# Iterable判断是否为可迭代
f = isinstance(lis2, Iterable)
print(f)
# True

# 整型不可迭代
f = isinstance(100, Iterable)
print(f)
# False

# 生成器可迭代
f = isinstance((x + 1 for x in range(10)), Iterable)
print(f)
# True
