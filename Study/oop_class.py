"""
2019.11.22 20:16
类 面向对象
"""


class Cat:
   # def __new__(cls, *args, **kwargs):
   #      print("__new__")

    def __init__(self):
        print("__init__")

    def __del__(self):
        print("__del__")

    def eat(self):
        print("eat")

tom = Cat()
tom.eat()

print("===")