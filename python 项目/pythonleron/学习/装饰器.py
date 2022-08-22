# 装饰器是程序开发中使用的功能，使用得当效率会得以提升
# 实现开放封闭原则  指规定已经实现的的功能代码不能被修改，但可以被扩展
"""
封闭：已实现的功能代码块
开放：对扩展开发
"""

# def foo():
#     print("foo")
#
#
# def func():
#     print("func")
# foo = func  将func的地址给foo重新赋值
# foo()   func
# 函数名仅仅是个变量，只不过指向了定义的函数，才能通过函数名（）调用


"""
装饰器：

功能：
1.引入日志  记录函数被调用的信息
2.函数执行时间的统计 
3.执行函数前预备处理
4.执行函数后清理功能
5.权限校验等场景
6.缓存

遵循开放封闭原则！！
"""


# 定义装饰器
def decorater(func):
    print('---------------->1')

    # 内部函数
    def wrapper():
        func()
        print('刷漆')
        print('铺地板')
        print('买家具')
        print('精装修')

    print('---------------->2')
    return wrapper


# 为某个函数做扩展
@decorater
# @decorater 会将house函数作为参数传参
# @decorater 也会把函数内部的返回值赋给house
def house():
    print('毛坯房')


"""
当调用house时
此时的house已经接收了返回值wrapper 所有相当于调用了wrapper
wrapper内部也调用了一次func（是@decorater将house本身的传进进来的值）
则会打印
毛坯房
刷漆
铺地板
买家具
精装修
"""
house()

# 当不调用house 也打印
# ---------------->1
# ---------------->2


# 装饰器传参
"""
带参数的装饰器
如果原函数有参数，内部函数也要带参数
"""


def decorater1(func1):
    def wrapper1(*a, **s):
        func1(*a, **s)
        print(1)

    return wrapper1


@decorater1
def house1(address):
    print(f'地址:{address}')


house1('beijing')


@decorater1
def changfang(address, area):
    print(f'地址是：{address},面积是:{area}')


changfang('shanxi', 100)


@decorater1
def hotal(address, name, number):
    print(f'地址是：{address},名字：{name,},房间:{number}')


hotal(address='7天', name='儒家', number=2001)

# 装饰器修饰有返回值的函数
"""
当原函数有返回值 在内部函数也要带上返回值
"""


def decorater2(func1):
    def wrapper2(*a, **s):
        r = func1(*a, **s)
        print(r)
        print(1)
        return 600000

    return wrapper2


@decorater2
def house2():
    print(22)
    return 100000


a = house2()
print(a)

# 如果装饰器带参数则多执行一轮的调用
"""
@decorater2(xx)
"""
