# set集合 与dict字典类似
"""
1.没有重复，无序的随机位置存放    没有下标
2.符号：{} {元素，元素，元素} =-----> 集合
        {} {key:value,{key:value} =-----> 字典

3.定义
空集合的声明 set()
"""
arr1 = {'flew'}
# print(type(arr1))       <class 'set'>

set1_1 = {}
set1_2 = ()
set1_3 = []
set1_4 = set()
# print(type(set1_1))     <class 'dict'>
# print(type(set1_2))     <class 'tuple'>
# print(type(set1_3))     <class 'list'>
# print(type(set1_4))     <class 'set'>

# 添加元素
set1_4.add('10')

# 合并
set1_4.update(arr1)
print(set1_4)
