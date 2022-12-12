"""
2019.11.23 16.39 - 16:44
单例模式

初始化
<__main__.Singleton object at 0x036B0950>
<__main__.Singleton object at 0x036B0950>
"""


class Singleton(object):
    # 单例对象引用
    instance = None

    # 记录初始化动作
    init_flag = False

    # 重写 new 方法
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    # 改写初始化方法
    def __init__(self):
        if Singleton.init_flag:
            return

        print("初始化")

        Singleton.init_flag = True


player1 = Singleton()
player2 = Singleton()

print(player1)
print(player2)
