"""
2019.11.29 20:53
飞机大战 Aircraft Wars

相关文件：
plane_main.py           游戏主程序
plane_sprites.py        游戏精灵子类
[planegame_class.png]   游戏类图（可选）
./images				游戏资源

游戏主程序：
封装主游戏类
创建游戏对象
启动游戏
"""

from plane_sprites import *


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化...")

        # 1. 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2. 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 3. 调用私有方法、精灵和精灵组的创建
        self.__create_sprites()
        # 4. 设置定时器时间 - 创建敌机 1s
        #  set_timer(eventid, milliseconds) -> None
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):
        # 创建背景精灵和精灵组
        back1 = Background()
        back2 = Background(True)

        self.back_group = pygame.sprite.Group(back1, back2)

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始...")

        while True:
            # 1. 设置刷新频率
            self.clock.tick(FRAME_PER_SEC)
            # 2. 事件监听
            self.__event_handler()
            # 3. 碰撞检测
            self.__check_collide()
            # 4. 更新/绘制精灵组
            self.__update_sprites()
            # 5. 更新显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            # 判断退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            # 创建敌机精灵，添加到组中
            elif event.type == CREATE_ENEMY_EVENT:
                model = random.randint(1, 2)
                enemy = Enemy(model)
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # # 捕获键盘按键 方式一，必须要弹起按键才算一次事件，操作灵活性大打折扣
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("right")

        # 捕获键盘按键 方式二，可连续移动，操作灵活性好
        # 返回所有按键的元组
        keys_pressed = pygame.key.get_pressed()
        # 判断按下了方向键，对应的值为1
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 5
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -5
        else:
            self.hero.speed = 0

    def __check_collide(self):
        # 英雄子弹精灵组 与 敌机精灵组 碰撞
        # groupcollide(groupa, groupb, dokilla, dokillb, collided=None): return dict
        # dokikk = True，发生碰撞的精灵将自动移除
        # collided: 计算碰撞的回调函数。如果没有指定，则每个精灵必须有一个Rect属性
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

        # 英雄精灵 与 敌机精灵组 碰撞
        # pygame.sprite.spritecollide(sprite, group, dokill, collided=None): return Sprite_list
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            # 英雄牺牲
            self.hero.kill()
            # 结束游戏
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == "__main__":

    # 创建游戏对象
    game = PlaneGame()

    # 启动游戏
    game.start_game()
