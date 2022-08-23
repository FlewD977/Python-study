class Cat:
    type = 'cat'

    # 通过__init__初始化特征
    def __init__(self, nickname, age, color):
        self.nickname = nickname
        self.age = age
        self.color = color

    # 动作等于方法
    def eat(self, food):
        print(f"{self.nickname}喜欢吃{food}")

    def catch_mouse(self, color, weight):
        print(f'{self.nickname}抓了一只{color}的，{weight}kg的老鼠')

    def sleep(self, hours):
        if hours < 5:
            print('keep sleep')
        else:
            print('WTF，go outside')

    def shiw(self):
        print(f'什么，他才{self.age}岁，它{self.color}的')


Cat_1 = Cat('花花', 13, 'blackinwucaibanl')
Cat_1.catch_mouse('red', 2)
