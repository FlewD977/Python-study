# 文件操作
"""
文件上传：
    系统函数：
        open() 打开具体的文件 不能打开文件夹
参数：
mode：  默认rt
    r w  纯文本文件
     rb wb  图片 音乐 纯文本 影片
buffering 缓存:
"""
# 文件读取
result1 = open(r"D:\python 项目\pythonleron\文件\ a1.txt")
print(result1)
# <_io.TextIOWrapper name='D:\\python 项目\\pythonleron\\文件\\ a1.txt' mode='r' encoding='cp936'>

# test1 = result1.read() #读取所有内容
# print(test1)
# # helo

test1_1 = result1.readable()  # 判断文件是否可读
print(test1_1)
# True

# while True:
#     test1_2 = result1.readline()  # 如果前面已经使用read函数读取过该文件了 再使用readline则为空
#     print(test1_2)  # 读一行默认换行
#     # helo
#     if not test1_2:
#         break
# helo
#
# flew
#
# nihao

test1_3 = result1.readlines()  # 一次读取多行
print(test1_3)
# <class 'list'>
# ['helo\n', 'flew\n', 'nihao']
for i in test1_3:
    print(i)
# helo
#
# flew
#
# nihao
result1.close()  # 关闭流 清空缓存区

result2 = open(r"C:\Users\Flew\Pictures\Saved Pictures\wallhaven-1jempv.jpg", "rb")
# 加r防止字符转义
print(result2)

result2_1 = result2.read()
# print(result2_1)
# 图片的16进制

result2.close()

# 文件写入

"""
mode是“w” 表示就是写操作
从开启流 到关闭流 中间的所有操作都为一次操作
方法：
    write（内容） 每次都会将原来的内容清空，然后写当前的内容
    
"""
result3 = open(r"D:\python 项目\pythonleron\文件\ a1.txt", "w")

wite = result3.write('123')  # 默认重写
print(wite)  # 写入字符串长度
# 3

wite1 = result3.writelines('hello world')

# 123hello world

result3.writelines(["你好李焕英\n", "你好xxx", "\n"])  # 需要单独加换行转义字符
# 123hello world你好李焕英
# 你好xxx
#

result3.close()  # 若关闭资源 再去调用就会报错
# wite = result3.write('123')
# ValueError: I/O operation on closed file.


"""
追加内容
mode a 
"""
result3 = open(r"D:\python 项目\pythonleron\文件\ a1.txt", "a")
result3.write('flew')
# 123hello world你好李焕英
# 你好xxx
# flew

result3.close()  # 若关闭资源 再去调用就会报错

# 文件的复制
"""
源文件：
目标文件：
with 结合open 使用 ，可以帮助我们自动释放资源
"""
# result4 = open(r"C:\Users\Flew\Pictures\Saved Pictures\wallhaven-1jempv.jpg", "rb")
# result4.close()

with open(r"C:\Users\Flew\Pictures\Saved Pictures\wallhaven-1jempv.jpg", "rb") as result4:
    resullt1 = result4.read()

    with open(r'D:\python 项目\pythonleron\文件\a2.jpg', 'wb') as result5:
        resullt1_1 = result5.write(resullt1)

# 批量复制
"""
os模块：
os中的函数
os.getcwd()    得到当前文件所在的文件夹路径 与dirname类似
os.listdir()    返回指定目录下所有的文件和文件夹的名字 返回为list
os.mkdir()      在指定路径下创建文件夹
os.rmdir()      删除指定路径下的文件夹 不能删除非空的文件夹
os.remove()     删除指定文件
os.chdir()      改变到指定目录


path中的函数
os.path 表示对系统内的内容进行操作
os.path.dirname(__file__) __file__表示当前文件 dirname表示获取目录
os.path.join(xxx,"xxx") 返回的是拼接后的新路径 允许拼接多个字符

os.path.absolute()  判断是否为绝对路径 
os.path.abspath()   得到指定文件/当前文件的绝对路径

os.path.split()     返回一个元组，元组内一个元素是文件路径，另一个元素是文件名 
os.path.splitext()  返回一个元组，元组内一个元素是文件名路径，另一个元素是文件后缀
os.path.getsize()   返回文件大小 单位是字节

os.path.isabs()     判断是否为绝对路径
os.path.isfile()    判断是否为文件
os.path.isdir()     判断是否为文件夹



"""
import os

# print(os.path)
# # <module 'ntpath' from 'D:\\python\\lib\\ntpath.py'>
#
# print(os.path.dirname(__file__))  # 获取当前文件所在的文件绝对路径
# # D:\python 项目\pythonleron\学习
#
# path = os.path.dirname(__file__)
# print(os.path.join(path, 'a3.jpg'))
# # D:\python 项目\pythonleron\学习\a3.jpg
#
# with open(r"C:\Users\Flew\Pictures\Saved Pictures\wallhaven-1jempv.jpg", "rb") as result4:
#     resullt1 = result4.read()
#
#     # 可以看到真实路径
#     # path = os.path.dirname(__file__)
#     # path1 = os.path.join(path, "a3.jpg")
#
#     # 若无法看到真实路径
#     print(result4.name)
#     # C:\Users\Flew\Pictures\Saved Pictures\wallhaven-1jempv.jpg
#     file11 = result4.name
#     fail1_1 = file11[file11.rfind("\\") + 1:]
# print(fail1_1)
# wallhaven-1jempv.jpg

# fail1_1 = file11[file11.rfind("\\"):]
# \wallhaven-1jempv.jpg
# print(fail1_1)
#
# with open(fail1_1, 'wb') as result5:
#     result5.write(resullt1)

# 删除文件夹下多个文件
# path1 = "../文件/pp1"
# flielist = os.listdir(path1)  # 拿到文件下的所有文件名
# print(flielist)
# for file in flielist:
#     pathj = os.path.join(path1, file)
#     os.remove(pathj)
# else:
#     os.rmdir(path1)

# 文件复制
s1_path = r'C:\Users\Flew\Pictures\Saved Pictures'
s2_path = r"D:\python 项目\pythonleron\文件\native"


# 封装


def copy_file(s1, s2):
    # 判断是否为文件夹
    if os.path.isdir(s1) and os.path.isdir(s2):
        # 取出文件夹列表
        filelist1 = os.listdir(s1)

        for file in filelist1:
            # 在原路径的基础上拼接
            path = os.path.join(s1, file)
            # 判断是否为文件夹
            if os.path.isdir(path):
                # 更改目的路径
                s2_path1 = os.path.join(s2, file)
                # 创建文件夹
                os.mkdir(s2_path1)
                copy_file(path, s2_path1)
        else:
            with open(path, "rb") as fileresult:
                t1 = fileresult.read()
                path1 = os.path.join(s2, file)

                with open(path1, "wb") as fileresult1:
                    fileresult1.write(t1)
    else:
        print("复制完毕")


copy_file(s1_path, s2_path)
