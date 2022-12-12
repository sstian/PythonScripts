"""
2019.11.22 21:28 - 21:45
士兵突击

冲啊...[许三多]
[AK47] 突了一下...[49]
"""

class Gun:
    def __init__(self, model):
        # 枪的型号
        self.model = model

        # 子弹的数量
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count  += count

    def shoot(self):
        # 1. 判断子弹数量
        if self.bullet_count <= 0:
            print("[%s] 没有子弹了..." % self.model)
            return

        # 2. 发射子弹 -1
        self.bullet_count -= 1

        # 3. 提示发射信息
        print("[%s] 突了一下...[%s]" % (self.model, self.bullet_count))


class Soldier:
    def __init__(self, name):
        # 1. 士兵的名字
        self.name = name

        # 2. 枪 - 新兵没有枪
        self.gun = None

    def fire(self):
        # 1. 判断士兵是否有枪
        if self.gun is None:
            print("%s 还没有枪..." % self.name)
            return

        # 2. 高喊口号
        print("冲啊...[%s]" % self.name)

        # 3. 让枪装填子弹
        self.gun.add_bullet(50)

        # 4. 让枪发射子弹
        self.gun.shoot()


ak47 = Gun("AK47")
duo = Soldier("许三多")
duo.gun = ak47
duo.fire()
