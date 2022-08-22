# 列表推导式指得到列表的一种方式
"""
旧的列表 通过推导 得出新的列表
格式：[i for i in 可迭代的变量（旧列表）]
"""
list1 = []
for i in range(1, 21):
    list1.append(i)
# print(list1)        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

list2 = [i for i in range(1, 21)]
# print(list2)        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# 格式2
"""
list=[i for i in range(x) if 条件]
"""
list3 = [i for i in range(1, 21) if i % 2 == 0]
# print(list3)        [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 格式3
"""
list=[结果1 if 条件 else 结果2 for 变量 in 可迭代变量]
"""
# 如果是h开头的则首字母大写 如果不是则全部大写
list4_4 = ['hai', 'hello', 'flew', 'nihao', 'hegin']
list4 = [word.title() if word.startswith('h') else word.upper() for word in list4_4]
# print(list4)        ['Hai', 'Hello', 'FLEW', 'NIHAO', 'Hegin']


# 集合推导式
"""
{}类似列表推导式，在列表推导式的基础上添加了去除重复项的功能
格式：
{x for x in list}
"""
list5_5 = [1, 2, 3, 1, 2, 3, 4, 5, 6, 4, 98, 58, 7, 7, 9, 22, 2, 1]
set1 = {x + 1 for x in list5_5 if x > 5}
print(set1)
# {1, 2, 3, 4, 5, 6, 98, 7, 9, 22, 58} 集合不能又重复的

# 表达式x+1
# {2, 3, 4, 5, 6, 7, 99, 8, 10, 23, 59}


# 字典推导式
"""

"""
dict1 = {'a': "A", 'b': "B", 'c': "C", 'd': 'C'}
newdict = {value: key for key, value in dict1.items()}
# items 指一对儿一对儿的取出
print(newdict)
# {'A': 'a', 'B': 'b', 'C': 'd'}
# 字典中不可能存在两个同意的KEY，所以遇到相同的会将后面的value覆盖到当前key
