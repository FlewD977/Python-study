"""
类似结构体

先定义class
所有的类名要求首字母大写 ，多个单词使用驼峰式命名 默认继承object
ValudeError

类是一个模型 使用类构建对象
class 类名 (父类)可加可不加
    属性
    方法
"""


class Demo(object):
    pass
    # 属性
    brand = "iphone"


print(Demo)
# <class '__main__.Demo'>


# 使用class创建对象
cl1 = Demo()
print(cl1)
# <__main__.Demo object at 0x000001A3D8669A90>

# 读取属性
print(cl1.brand)
# iphone

# 修改属性
cl1.brand = '华为'
print(cl1.brand)

# 华为


# 类中的方法
"""
1、普通方法  只能通过类调用方法不能直接调用
    格式：def name(self[参数，参数]) #self表示调用该方法的当前实例对象 调用该方法就将自身作为参数传给self
2、类方法
    定义需要依赖装饰器 @classmethod
    类方法中的参数不是对象而是当前类 同时也不依赖与对象
    类方法只能使用类属性 可以用类名去调用
    作用：
        因为只能访问类属性或方法，所以会在对象创建之前，完成一些功能
3、静态方法
    
    
"""


# 普通方法
class Phone():
    brand = "iooq"
    price = 5369
    type = 'a 10'

    # Phone类中的方法call
    def call(self):
        print(self)  # <__main__.Phone object at 0x000001900B625F70>
        print('call me...')
        print('留言：', self.noth)  # 不能保证每个self中都存在noth 所以报阴影
        for person in self.adddress_list:
            print(f'通讯薄：{person}')

    # 魔术方法之一解决阴影问题   __名字__()称为魔术方法  用户根据系统关键字定义后，无需调用方法系统会执行
    def __init__(self):  # init代表初始化
        print('-' * 30)  # ------------------------------
        # 动态的在self空间添加了多个属性
        self.dymict = '我出现了'
        self.dymiced = '我消失了'

    def dun(self, city):
        print(f'你在哪儿：{self.dymict}在：{city}')  # 阴影就消失了


ph1 = Phone()
print(ph1)  # <__main__.Phone object at 0x000001900B625F70>
ph1.noth = '我不好'
ph1.adddress_list = {'1110': 'flew', '1111': 'wushim', '1112': 'hello'}
ph1.call()

ph2 = Phone()
ph2.noth = 'hello 你好'
ph2.adddress_list = {'2220': 'flew', '2222': 'wushim', '2223': 'hello'}

ph2.call()
ph2.dun('山西')


# 类方法
class dog:
    aa = 'a'

    def __init__(self, nickname):
        self.nickname = nickname  # 初始化

    def run(self):  # self依赖与对象
        print(f'{self.nickname}在院子里跑')  # 阿黄在院子里跑

    def eat(self):
        print('runing')
        self.run()  # 只能通过self调用

    @classmethod
    def test(cls):
        print(cls)  # <class '__main__.dog'>
        # print(cls.nickname)  # type object 'dog' has no attribute 'nickname'


print('*' * 30)
d = dog('阿黄')
d.run()
d.test()

dog.test()  # 可以使用类名调用类方法 或属性

# dog.aa


# 静态方法
"""
    类似类方法
        需要装饰器@staticmethod
        静态方法无需带任何参数（cls，self）
        也只能访问类的属性和方法 对象是无法访问的
        加载时机和类方法一样
"""


class Person1():
    __age = 15  # __指将属性私有化 外界是无法调用的

    # def show(self):
    #     print(f'年龄{Person1}')
    def __init__(self, name):
        self.name = name

    @classmethod
    def update_age(cls):
        cls.__age = 20
        print('-' * 30)

    @classmethod
    def show_age(cls):
        print(f'更改后{cls.__age}')

    @staticmethod
    def test():
        print('------------静态方法')
        # print(self.name) self对象不能出现在静态方法中
        print(Person1.__age)  # 不依赖于cls 那就用类名来调用


# Person1.age = Person1.age + 1  # 16
# print(Person1.age)  # 私有化后type object 'Person1' has no attribute 'age'

Person1.update_age()
Person1.show_age()  # 更改后20 要先调用update_age后才能更改

Person1.test()
# ------------静态方法
# 20


# 总结
"""
类方法 静态方法
不同之处：
    装饰器不同
    类方法有参数，静态方法无参数
相同之处：
    只能访问类的属性和方法，对象是无法访问的
    都可以通过类名调用
    都可以在创建对象之前使用，因为是不依赖于对象
    
普通方法
不同之处：
    没有装饰器
    普通方法需要对象，因为每个普通方法都有一个self
    只有创建了对象才可以调用普通方法，否则无法调用
"""

# 魔术方法
"""
就是类/对象中的方法，于普通方法不同的是，普通方法需要调用，魔术方法是在特定时刻自动调用

常用的魔术方法：
__init__:初始化魔术方法，初始化对象时触发，用于初始化对象的成员  重点
__new__:实例化的魔术方法，在实例化对象时触发，
__call__:调用对象的魔术方法，将对象当作函数调用时触发 对象（） 将复杂的步骤进行合并操作减少调用的步骤方便使用
__del__:析构魔术方法，当对象没有任何变量引入时被触发，使用完对象时回收资源 
    注：python在运行完成后会自动调用底层的del来清空所有的内存占用，若自己定义了del则会覆盖底层的，通常不写
__str__:打印时返回对象的变量，打印对象名时触发     重点
    注:这个方法不能和__new__一起使用不然会报错 找不到属性 因为__str__也会重写和new冲突
"""

import sys  # 系统模块


class show_magic():
    def __init__(self, name1):
        print('init', '-' * 30)  # 3 init ------------------------------
        self.name1 = name1
        print(self.name1)  # 4 jack
        print(self)  # 5 <__main__.show_magic object at 0x10ab5b7c0>

    def __new__(cls, *args, **kwargs):  # 如果在init后写了new类会重新覆盖 所以只打印了分割线
        print('-' * 30)  # 1
        position = object.__new__(cls)  # 0x10ecaf7c0
        print(position)  # 2 <__main__.show_magic object at 0x10ecaf7c0>
        return position

    # 进入class new会先执行 实例化也就是开辟了一个新的空间或者说创建了一个新的对象
    # return 返回的则是新开辟的空间 当执行完new init会继续执行 self接收new返回出的空间 处理完后返回给外层调用的
    # 若不return 则init不会执行 因为拿不到地址
    # new+init 才是完整的构造器 ，参考JAVA，先new对象，再初始化

    def __call__(self, *args, **kwargs):
        print('-' * 30, "call")
        print(*args)  # hello

    # def __del__(self):
    #     print('-' * 30, "del")

    # def __str__(self):  # 注意这个方法不能和__new__一起使用不然会报错 找不到属性
    #     return 'name:' + self.name1  # return是必须加的  naem:word


s = show_magic('jack')
# ------------------------------
# show_magic.__new__() 类中不写，也可以在外面调用new，如果类里写了new系统的new就会失效，转而执行类里的new
print(s)  # <__main__.show_magic object at 0x10a2fb7c0>

# 将对象当作函数名调用 不用s.xxxx去调用
s()  # ------------------------------ call
s('hello')

print(sys.getrefcount(s))  # 查找s的地址有几块引用
# 2 本身调用这个方法还算一次

# ss = s
# del ss  # 代表解除ss对s引用对那块儿内存空间地址 但是其他的引用不受影响
# print('删除ss', s.name1)  # jack
# # ------------------------------ del 代表执行了 __del__


print(s)  # 单纯打印的只是一个地址
# __str__可以在打印对象名时将变量内容打印出来，给予开发者更多的信息
# name:jack

"""
总结
类中的方法：

普通方法
def func(self):   self对象
    pass

类方法
@classmethod
def func(cls):  cla类
    pass

静态方法
@staticmethod
def func():     无需参数
    pass
    
魔术方法
__init__
__str__
"""
