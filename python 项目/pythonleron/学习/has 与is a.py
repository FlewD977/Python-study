"""
has a :是如果A中有B，那么，B就是A的组成部分  补集
is  a ：是如果A是B，那么B就是A的基类     子集
"""


class Computer():
    pass


class Book():
    pass


class Student():
    def __init__(self, name, computer, book):
        self.name = name
        self.computer = computer
        self.book = []
        self.book.append(book)
