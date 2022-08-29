# 私有化
"""
以为属性私有化后外界无法访问也无法修改
封装到类：
    1、私有化属性
    2、定义公有的set方法为了赋值 get方法为了取值
        使用对象方法修改私有化属性
优点：隐藏属性，不被外界随意修改
缺点：
"""


class students():

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.__score = 60  # 私有化属性

    def __str__(self):
        return f'学生姓名是{self.name},他今年{self.age},他是{self.sex}生,成绩是{self.__score}'

    #     定义set方法
    def Set_nuber(self, score):
        if self.__score > 0 and self.__score < 120:
            self.__score = score

    #       定义get方法
    def Get_nuber(self):
        return self.__score


s1 = students('张三', '20', '男')
print(s1)  # 学生姓名是张三, 他今年20, 他是男生, 成绩是60

s1.__score = 90  # 无法更改
print(s1)  # 学生姓名是张三,他今年20,他是男生,成绩是60

s2 = students('王五', '20', '女')
s2.Set_nuber(90)
print(s2)  # 学生姓名是王五,他今年20,他是女生,成绩是90

# 在开发中私有化的处理
"""
装饰器 
@property  
作用：代替set get

# 取值
格式
@property 
def name(self):
可以将def name 当作属性去调用

# 赋值
name.setter #name函数的setter方法来实现赋值
def name(self, name): 

注意：一定要先定义取值，才能使用取值里的函数name，去使用赋值的setter的方法 
"""


class students_1():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.__score = 60

    def __str__(self):
        return f'学生姓名是{self.name},他今年{self.age},他是{self.sex}生,成绩是{self.__score}'

    @property
    # 取值
    def score(self):  # name不能随便定义，会报阴影  必须定义为私有化属性的名字
        return self.__score

    # 赋值
    # @property.setter descriptor 'setter' for 'property' objects doesn't apply to a 'function' object
    @score.setter
    def score(self, score):
        pass


s2 = students_1('赵六', '22', '男')
print(s2.score)  # 可以当作属性去调用，不需要家括号

s2.score = 90
