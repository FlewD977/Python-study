"""
异常处理
try:
    可能出现异常的代码
except 错误类型:
    如果有异常执行的代码，通常会结合报错类型使用
    如果遇到指定的错误类型才会执行代码
finally:
    无论是否存在异常都会被执行的代码
    通常使用场景是关闭流，以及操作数据库都需要关闭，保证内存不被占用

情况一：
    try：
        有可能产生多种异常
    except 异常的类型1:
        一个except就不够精准
    except 异常的类型2:
        那就多个except
    except 异常的类型x:
        如果是多个except：异常类型的顺序需要注意，最大的Exception要放到最后
        pass


情况二：
    try：
        有可能产生多种异常
    except Exception as err: #系统会识别错误类型 并且打印出来
        print("打印错误：",err)
"""

#
# def func():
#     try:
#         n1 = int(input('请输入第一个数字'))
#         n2 = int(input('请输入第二个数字'))
#         sum = n1 + n2
#         print('sum')
#     # except BaseException:
#     #     print('必须输入数字')
#     except Exception:
#         print('请输入：')
#
#
# func()
# # 当加上try和except后 如果前面遇到了异常并不会影响后面的代码继续执行
# print('-----------')
#
#
# def filfuntion():
#     try:
#         n1 = int(input('请输入第一个数字'))
#         n2 = int(input('请输入第二个数字'))
#         sum = n1 + n2
#         print('sum')
#         # 文件操作
#         with open(r"d:\python 项目\pythonleron\文件\ a1.txt", "wb") as filee:
#             filee.write(f"本次的运算结果是:{sum}")
#
#     except FileNotFoundError:
#         pass
#     # except Exception:  # Exception是所有错误的根方法 若不知道会出现什么错误则可以写这个方法
#     #     # 类似switch case defined
#     #     pass
#     except Exception as err:  # 会打印错误的原因
#         print("出错了", err)
#

"""
try:
    pass
except:
    pass
else: #只要前面的代码完美执行则会执行else finally是不论成功与否都会执 行
    pass 
"""


def funnel():
    stream = None
    try:
        stream = open(r"d:\python 项目\pythonleron\文件\ a1.txt")
        container = stream.read()
        print(container)
    except Exception as err:
        print(err)
    finally:
        print("准备关闭")
        if stream:
            stream.close()  # stream是在try里的内部变量 需要在外进行声明变为全局变量


funnel()

# 抛出异常
"""
raise 主动抛出异常

"""


# 注册 用户名必须6位
def register():
    username = input("请输入用户名：")
    if len(username) < 6:
        raise Exception('用户长度必须六位以上')

    #         raise Exception('用户长度必须六位以上')
    # Exception: 用户长度必须六位以上
    #
    # Process finished with exit code 1

    else:
        print('输入的用户名是：', username)


try:
    register()
except Exception as e:
    print(e)
    print('注册失败')
else:
    print('注册成功')
