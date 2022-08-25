class Pers():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '测试' + self.name


p = Pers('word')
print(p)
