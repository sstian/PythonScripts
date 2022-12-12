"""
2019.11.08 23:00 - 23:21
猜拳
"""
# 导入工具包
import random

player = int(input("请出拳 石头(1) 剪刀(2) 布(3): "))
computer = random.randint(1, 3)

if((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("欧耶，电脑弱爆了~")
elif player == computer:
    print("心有灵犀，平手。")
else:
    print("我要和你大战三百回合，居然输了！")