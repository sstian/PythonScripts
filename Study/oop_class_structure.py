"""
2019.11.23 15:24
类的结构：
类属性 类方法，实例属性 实例方法，静态方法

历史记录 0
帮助信息；防御僵尸进入城堡
小明 开始游戏啦...
"""


class Game(object):
    # 类属性
    # 历史最高分
    top_score = 0

    # 类方法
    @classmethod
    def show_top_score(cls):
        print("历史记录 %d" % cls.top_score)

    #静态方法
    @staticmethod
    def show_help():
        print("帮助信息；防御僵尸进入城堡")

    # 初始化方法 定义实例属性
    def __init__(self, player_name):
        # 实例属性
        self.player_name = player_name

    # 实例方法
    def start_game(self):
        print("%s 开始游戏啦..." % self.player_name)


# 1. 查看历史最高分
Game.show_top_score()

# 2. 查看游戏帮助信息
Game.show_help()

# 3. 创建游戏对象
game = Game("小明")
game.start_game()
