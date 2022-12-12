"""
2019.11.29 20:52
游戏常量
封装游戏精灵子类 GameSprite(pygame.sprite.Sprite)
封装游戏背景精灵类，实现背景交替滚动 Background(GameSprite)
封装敌机精灵类，使用定时器添加敌机 Enemy(GameSprite)
封装英雄精灵类 Hero(GameSprite)
封装子弹精灵类 Bullet(GameSprite)

定时器：每隔一段时间，执行一些动作
1> 定义 定时器常量 eventid
2> 初始化方法中，调用 set_timer() 设置定时器事件
3> 游戏循环中，监听定时器事件

导入模块顺序：
官方标准模块 -> 第三方模块 -> 应用程序模块
"""

import random
import pygame


# 游戏常量
# 屏幕大小
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器事件
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        # 调用父类方法
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        # get_rect(**kwargs) -> Rect
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕垂直方向上移动
        self.rect.y += self.speed

# 背景交替滚动：游戏背景 连续不断变化，游戏主角 位置保持不变
# 面向对象设计原则，将对象的职责封装到类的代码内部，
# 尽量简化程序调用一方的代码


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        """
        :param is_alt: 判断是否是另一张图像。
        False: 第一张图像，需要与屏幕重合
        True: 另一张图像，在图像的正上方
        """
        # 1. 调用父类方法实现精灵的创建(image/rect/speed)
        super().__init__("./images/background.png")

        # 2. 判断交替图像，是，需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 1. 调用父类的方法实现
        super().update()

        # 2. 移出屏幕，设置图像到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self, model):
        """

        :param model: 敌机类型
        """
        # 1. 父类方法
        self.model = model
        if 1 == model:
            super().__init__("./images/enemy1.png")
        elif 2 == model:
            super().__init__("./images/enemy2.png")
        # 2. 初始随机速度
        self.speed = random.randint(1, 3)
        # 3. 初始随机位置
        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 1. 父类方法，垂直飞行
        super().update()
        # 2. 判断飞出屏幕，需要从精灵组删除
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        # print("敌机挂了 %s" % self.rect)
        pass


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):
        # 1. 父类方法
        super().__init__("./images/me1.png", 0)
        # 2. 设置英雄初始值
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 3. 创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 英雄在水平方向移动
        self.rect.x += self.speed

        # 控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        # 一次发射三颗子弹
        for i in (0, 1, 2):
            # 1. 创建子弹精灵
            bullet = Bullet()
            # 2. 设置精灵的位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            # 3. 添加精灵到精灵组
            self.bullets.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):
        # 父类方法
        super().__init__("./images/bullet1.png", -2)

    def update(self):
        # 父类方法，子弹垂直飞行
        super().update()

        # 判断子弹飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        pass
