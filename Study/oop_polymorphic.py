"""
2019.11.22 23:10
多态，前提：继承+重写父类方法

小明 和 哮天犬 快乐地玩耍...
哮天犬 飞到天上玩耍...
"""

class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 玩耍..." % self.name)


class Tian(Dog):
    def game(self):
        print("%s 飞到天上玩耍..." % self.name)

class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和 %s 快乐地玩耍..." % (self.name, dog.name))
        dog.game()


# wang = Dog("旺财")
wang = Tian("哮天犬")
ming = Person("小明")
ming.game_with_dog(wang)
