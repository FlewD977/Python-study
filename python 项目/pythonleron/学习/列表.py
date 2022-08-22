"""
列表定义
1.空列表: []
2.列表元素：[int,str,bool,float,[]] 可以套列表
3.两套下标索引机制获取元素
"""
import random

list1 = ['flew', 'hello', 'nihao', 'flew']
# 切片
# print(list1[:2])        ['flew', 'hello']包前不包后

# 添加
list1.append('wobuhao')
print(list1)

# 合并
list2 = [1, 2, 3, 4, 56]
# print(list2 + list1)        [1, 2, 3, 4, 56, 'flew', 'hello', 'nihao', 'wobuhao']
# list1.extend(list2)
# print(list1)                ['flew', 'hello', 'nihao', 'wobuhao', 1, 2, 3, 4, 56]

# 删除（）/清空/弹出（下标/del
list2.remove(56)
print(list2)
list2.clear()
print(list2)
# list2.pop(8)  # 若下标超出会报错 若不传值则是从后往前依次删除

list3 = list2
list3.append(90)  # 因为python的内存优化 list3拿到的是list2的内存地址类似于指针 所以对list3操作会使list2变化
print(list3)  # [90]
print(list2)  # [90]

# del list3  del 回收list名 若没有将list2的地址给list3 del list2 将直接删除整list   clear是清空list内的元素
# print(list3) NameError: name 'list3' is not defined
# del list2
# print(list2)    NameError: name 'list2' is not defined

# 关键字in
"""
判断元素是否存在list中
"""
if 56 in list2:
    print("存在")
else:
    print("不存在")

"""
删除多个元素
若要删除的元素挨着 则会漏删 
原理是for根据下标来进行遍历的 若删掉第一个flew 则第二个flew变为之前的flew的下标 而for会进行下一个下标因此而跳过一个
"""
list1_1 = ['flew', 'hello', 'nihao', 'flew', 'flew', 'flew']

for i in list1_1:
    if i == 'flew':
        list1_1.remove(i)
else:
    if i == 'flew':
        list1_1.remove(i)
print(list1_1)
# 解决
n = 0
while n < len(list1_1):
    if list1_1[n] == 'flew':
        list1_1.remove('flew')
    else:
        n += 1

print(list1_1)
# ['hello', 'nihao']

# 查找
"""
1.元素 in 列表      返回bool类型
2.元素 not in 列表      返回bool类型
"""

# 排序
"""
sort()
默认升序 通过reverse控制
"""
numbers = []
for h in range(8):
    ran = random.randint(1, 20)
    numbers.append(ran)
print(numbers)

numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
