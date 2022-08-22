# 字典是无序的 是可变的数据类型
"""
dict = {key:val}
key是不能重复的 value是可以重复的
"""
# 定义
dict1 = {}

# 添加
dict1['name'] = 'flew'
dict1['age'] = 18
# print(dict1)        {'name': 'flew', 'age': 18}

# 修改
"""
key是不能修改的 只能添加和删除
value是可以修改的
"""
dict1['price'] = 20.5
dict1['折扣'] = '8折'
dict1['price'] *= 0.8
print(dict1)

# 删除
""""
.clear()    清空
.pop(‘key’) 根据key删除键值对 返回值是value  
.popitem()  删除最后一个键值对 返回的元组中存放删除的元素
del dict['key'] 类似于pop     
"""

# 遍历和查询
"""
get('key','找不到')  根据key得到value 若找不到则返回找不到默认是None
"""

print(dict1.get('price'))

"""
for i in dict :
    print(i)
使用for遍历只会打印key

for i in dict.values() :
    print(i)
则打印出所有的value 存放与列表中    
.keys()同理

for i in dict.items() :
    print(i)
则打印所有的键值对 存放与列表中

for k,v in dict1.items():
    print(k)
    print(v)
更加灵活的取出键值对
"""
for k, v in dict1.items():
    print(k)
    print(v)

# 合并
dict2 = {'a': '1', 'b': '2'}
dict2.update(dict1)
print(dict2)
