"""
2019.11.22 21:02 - 21:11
爱跑步的人儿

我叫 ming，体重 75.00 公斤
ming 爱跑步，锻炼身体
ming 是吃货，吃饱再减肥
我叫 mei，体重 45.00 公斤
mei 爱跑步，锻炼身体
mei 是吃货，吃饱再减肥
"""


class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我叫 %s，体重 %.2f 公斤" % (self.name, self.weight)

    def run(self):
        print("%s 爱跑步，锻炼身体" % self.name)
        self.weight -= 0.5

    def eat(self):
        print("%s 是吃货，吃饱再减肥" % self.name)
        self.weight += 1


ming = Person("ming", 75.0)
print(ming)
ming.run()
ming.eat()

mei = Person("mei", 45.0)
print(mei)
mei.run()
mei.eat()