arr = '123456'
# 索引机制
"""
        1 2 3 4 5 6
正向索引 0 1 2 3 4 5
反向索引 -6 -5 -4 -3 -2 -1  当字符串过长 但只需要索引尾部元素时
"""

# 切片操作
"""
格式：字符串[start:end:step] start默认是0 但是end是n+1 step步长默认是1 正数为从左向右 负数为从右向左
"""
# print(arr[1:4])   234     start也可以省略不写
# print(arr[-3:6])    456   end也可以省略不写默认是末尾
# print(arr[::2])       135
# print(arr[::-3])        63


arr2 = 'https://i0.hdslb.com/bfs/feed-admin/a3c9630fe91464d96c48b97b2e71696f1cd4662a.jpg@976w_550h_1c.webp'
# 查找操作
# index 与find效果一样 但是区别是index找不到会报错
"""
find()
从左向右查找 查找到后则不会继续 
若没有找到 则返回-1
也可以传一个字符串 返回的值是找到的首字符的下标
"""
# image_name = arr2.find('-')  # 代表这个字符在第29个下标
# # print(image_name)   29
# print(arr2[image_name + 1:])

"""
rfind()
从右向左查找
若没有找到 则返回-1
"""
# r_image_name = arr2.rfind('.')
# print(arr2[r_image_name:])

"""
count()
计算出现次数
"""
# print(arr2.count('2'))


arr3 = 'a3c9630fe91464d96c48b97b2e71696f1cd4662a'
# 判断操作  返回的都是布尔类型
"""
startswith()
判断字符串是否以‘xxx’开头
endswith()
判断字符串是否以‘xxx’结尾
"""
# print(arr3.startswith('b'))   False
# print(arr3.endswith('gif'))     False

"""
isalpha()   
判断字符串是否由纯字符组成   返回True、False
isdigit()
判断字符串是否由纯数字组成   返回True、False
isalnum()
判断字符串是否由字符或数字组成   返回True、False
isspace()
判断字符串是否由空格组成   返回True、False
"""
arr3_1 = 'asdasdasdfxcv'
# print(arr3.isalpha())       False
# print(arr3_1.isalpha())     True

arr3_2 = "123456"
# print(arr3.isdigit())       False
# print(arr3_2.isdigit())     True

# print(arr3.isalnum())       True

arr3_3 = '    '
arr3_4 = ''
# print(arr3_3.isspace())     True
# print(arr3_4.isspace())     False


# 替换操作
"""
替换replace
替换字符串中的指定字符,指定次数
"""
arr4 = 'hello word nihao flew!!!'
print(arr4.replace('!', '#', 1))  # old str ，new str，次数
# hello word nihao flew#!!


# 切割操作
"""
切割split('分割符',1)
按照指定方法,指定次数正向切割后会将结果存入列表list中
反向切割rsplit('分隔符',1)
按照指定方法,指定次数反向切割后会将结果存入列表list中
行切割splitlines()
按行切割
"""
arr5 = 'hello word nihao flew！'
print(arr5.split(' '))
# ['hello', 'word', 'nihao', 'flew！']
print(arr5.rsplit(' ', 1))
# ['hello word nihao', 'flew！']

# 替换大小写操作
"""
title()
每个单词首字母大写   空格区分
upper()
所有字符大写
lower()
所有字符小写
"""
arr6 = 'flew hello'
# print(arr6.title())   Flewhello Flew Hello
# print(arr6.upper())     FLEW HELLO
# print(arr6.lower())        flew hello


# 空格处理
"""
strip()
删除头尾的空格 同理lstrip()左侧 rstrip()右侧
center()
指定空格字符并居中对齐
"""
arr7 = ' nihao    '
# print(arr7.strip())     nihao
arr7_1 = 'hello'
# print(arr7_1.center(20))       hello


# 拼接字符串
"""
join()

format()
第一种：'name{0}age{1}nickname{0}.format(name,age)' 
第二种：f'name{name}age{age}'
"""
