"""
2019.11.29 17:01
游戏窗口，绘制图像，游戏循环，事件监听

坐标系：原点(0, 0) 在左上角，x向右，y向下

pygame.Rect: x, y, left, top, right, bottom，
center, certerx, centery, size, width, height
[left == x, top == y, right == x + width, bottom == y + height]

游戏动画原理：
快速在屏幕上绘制图像，每秒绘制（帧）60次可达到 连续高品质 动画效果
电影：多张静止的电影胶片 连续、快速地播放

游戏初始化：
    设置游戏窗口，设置游戏时钟，创建精灵和精灵组
游戏循环：
    设置刷新帧率，事件监听，碰撞检测，更新/绘制精灵组，更新屏幕显示

事件 event：用户所做的操作，如：点击鼠标、按下键盘...
监听：捕获用户具体的操作，才能针对性地做出响应
"""


# import pygame

from plane_sprites import *

# Rect(left, top, width, height) -> Rect
# 英雄原点 100 500
# 英雄大小 120 125
# 120 125
hero_rect = pygame.Rect(100, 500, 120, 125)
print("英雄原点 %d %d" % (hero_rect.x, hero_rect.y))
print("英雄大小 %d %d" % (hero_rect.width, hero_rect.height))
print("%d %d" % hero_rect.size)

# 初始化
pygame.init()

# 游戏代码
# 创建游戏主窗口，创建内存屏幕数据对象 => “油画的画布”
# set_mode(size=(0, 0), flags=0, depth=0, display=0) -> Surface
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1> 加载图像数据
back = pygame.image.load("./images/background.png")

# 2> 绘制图像
# blit(source, dest, area=None, special_flags=0) -> Rect
screen.blit(back, (0, 0))

# 3> 更新屏幕，将画布结果一次性绘制在屏幕上
# update(rectangle=None) -> None

# 绘制英雄
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 500))

pygame.display.update()


# t1. 创建时钟对象
clock = pygame.time.Clock()

# h1. 记录英雄的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# s1. 创建敌机的精灵
enemy = GameSprite("./images/enemy1.png")
enemy2 = GameSprite("./images/enemy2.png", 2)
# s2. 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy, enemy2)

# 游戏循环：无限循环 => 游戏的正式开始
while True:

    # t2. 设置刷新帧率（屏幕绘制速度）
    clock.tick(60)

    # h2. 修改英雄位置
    hero_rect.y -= 5

    # 判断英雄的位置
    if hero_rect.y <= -126:
        hero_rect.y = 700

    # h3. 绘制图像
    screen.blit(back, (0, 0))
    screen.blit(hero, hero_rect)

    # s3. 精灵组调用，更新位置 与 图像绘制
    enemy_group.update()
    enemy_group.draw(screen)

    # h4. 更新显示，最先绘制背景，重新绘制所有图像
    pygame.display.update()

    # 事件监听，响应
    # pygame.event.get() 用户当前所做动作的事件列表
    for event in pygame.event.get():
        # 退出事件
        if event.type == pygame.QUIT:
            print("退出游戏...")
            pygame.quit()
            # 直接退出系统
            exit()

    # pass


# 退出
# pygame.quit()
