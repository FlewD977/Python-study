class Cat:
    type = 'cat'

    # ͨ��__init__��ʼ������
    def __init__(self, nickname, age, color):
        self.nickname = nickname
        self.age = age
        self.color = color

    # �������ڷ���
    def eat(self, food):
        print(f"{self.nickname}ϲ����{food}")

    def catch_mouse(self, color, weight):
        print(f'{self.nickname}ץ��һֻ{color}�ģ�{weight}kg������')

    def sleep(self, hours):
        if hours < 5:
            print('keep sleep')
        else:
            print('WTF��go outside')

    def shiw(self):
        print(f'ʲô������{self.age}�꣬��{self.color}��')


Cat_1 = Cat('����', 13, 'blackinwucaibanl')
Cat_1.catch_mouse('red', 2)
