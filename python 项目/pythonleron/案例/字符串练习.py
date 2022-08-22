# 模拟文件上传，键盘输入上传文件的名称（abc.jpg），判断文件名是否大于六位以上，扩展名是否是jpg格式 不是则提示上传失败
# 如果名字不满足条件，扩展名满足条件 则随机生成满足条件的名称 打印成功上传

# # 获取文件
# import random
#
# file = input('请输入图片文件全称')
#
# if file.endswith('jpg') or file.endswith('gif') or file.endswith('png'):
#     # 判断文件名称
#     name = file[:file.rfind('.')]
#     if len(name) < 6:
#         print("名称错误，将为您随机生成")
#         snm = random.randint(100000, 999999)
#         file = str(snm) + file[file.rfind('.'):]
#         print(f'上传文件{file}成功')
# else:
#     print("文件格式错误，上传失败")
# import random
#
# filename = ''
# s = 'qwertyuiopQWERTYUIOP1234560'
# for i in range(6):
#     filename += s[random.randint(0, len(s) - 1)]  # 不-1的话 会报错
#
# print(filename)


"""
用户名或者手机号码登录+密码
用户名：全部小写，首字母不能是数字，长度需六位以上
手机号：纯数字，长度11位
密码：六位数字

输入时同步判断是否符合条件直至条件符合
"""
name = input('请输入用户名或者手机号：')
flag = True
while flag:
    if (name.islower() and not name[0].isdigit() and len(name) >= 6) or (name.isdigit() and len(name) == 11):
        while True:
            pasaword = input("请输入密码：")
            if len(pasaword) == 6 and pasaword.isdigit():
                if (name == 'admin123' or name == '13663563149') and pasaword == '010528':
                    print('登录成功')
                    flag = False
                    break
                else:
                    print('密码错误！')
            else:
                print('密码格式错误，请重试！')

    else:
        print('用户名格式错误请重试！')
