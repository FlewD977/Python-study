"""
两个：1-6
1.玩游戏需要有金币 消耗5个
2.玩游戏赠送金币   1枚
3.充值获取  1：2比率
4.猜大小   猜对 获得2枚 猜错无 6点以上为大 以下为小
5.游戏结束：1.主动退出 2.没有金币退出
6.退出则打印金币数与游戏总数与胜率
"""
# 金币
import random

count=0
d_count=0
coins=0
if coins < 5:
    a=input(f"""
    抱歉您的金币数量不足无法进入游戏！！！
    ------------------------------
    您的金币数量为{coins}  本局游戏需要5个金币
    ------------------------------
            请充值：n    退出:0""")
    if a == 0:
        print('欢迎下次游玩')
    else:
        print('充值包为10元起充 10的倍数以此类推 ' )
    while True:
        money = int(input('请输入充值金额： '))
        if money % 10 == 0:
            coins += money*2
            print('充值成功')
            break
        else:
            print('充值失败请重新输入')
else:
    print('欢迎进入游戏')
while True:
    coins-=5
    num=random.randint(1,12)
    print(num)
    print('请下注 猜大/小')
    resut = input('您要压大请按大 压小请按小')
    if resut=='大' and num > 6:
        print(f'一共{num}点为大 恭喜您稳了 获得两枚金币')
        coins+=3
        count+=1
        b= input('是否继续游戏？\n 继续请按任意键 退出则按q')
        if b=='q':
            break
        else:
            if coins==0:
                print('抱歉您的金币不足以继续游戏')
                break
            else:
                print('马上开始下一轮游戏')
    elif resut=='小' and num <= 6:
        print(f'一共{num}点为小 恭喜您稳了 获得两枚金币')
        coins+=3
        count+=1
        b= input('是否继续游戏？\n 继续请按任意键 退出则按q')
        if b=='q':
            break
        else:
            if coins==0:
                print('抱歉您的金币不足以继续游戏')
                break
            else:
                print('马上开始下一轮游戏')
    else:
        if num<=6:
            print(f'一共{num}点为小 您的选择是大 再接再厉')
            count+=1
            d_count+=1
            coins+=1
            b= input('是否继续游戏？\n 继续请按任意键 退出则按q')
            if b=='q':
                break
            else:
                if coins==0:
                    print('抱歉您的金币不足以继续游戏')
                    break
                else:
                    print('马上开始下一轮游戏')
        else:
            print(f'一共{num}点为大 您的选择是小 再接再厉')
            count+=1
            d_count+=1
            coins+=1
            b= input('是否继续游戏？\n 继续请按任意键 退出则按q')
            if b=='q':
                break
            else:
                if coins==0:
                    print('抱歉您的金币不足以继续游戏')
                    break
                else:
                    print('马上开始下一轮游戏')

print(f'您的金币数为{coins}\n您一共进行游戏{count}局\n胜率为{float(d_count//count)}')