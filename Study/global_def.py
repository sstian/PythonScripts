"""
2019.11.21 19:47
全局变量

demo1: num = 99
demo2: num = 99
"""
g_num = 10
g_cnt = 0

def demo1():
    global g_num, g_cnt
    g_num = 99
    g_cnt = 37
    print("demo1: num = %d" % g_num)
    print("demo1: cnt = %d" % g_cnt)


def demo2():
    print("demo2: num = %d" % g_num)
    print("demo2: cnt = %d" % g_cnt)

demo1()
demo2()

g_dict = {
    "name": "ming",
    18: 188,
    1.75: 7.757,
    True: True,
    False: False,
    (1,): (1, 3,)
}

for name in g_dict:
    print(g_dict[name])
