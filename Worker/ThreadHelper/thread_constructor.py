"""
调用Thread类的构造器创建线程

直接对类 threading.Thread 进行实例化创建线程，并调用实例化对象的 start() 方法启动线程。
"""

import threading
import time


# 定义线程要调用的方法，*add可接收多个以非关键字方式传入的参数
def action(*add):
    for arc in add:
        # 调用 getName() 方法获取当前执行该程序的线程名
        print(threading.current_thread().getName() + " " + arc + "\n")
        time.sleep(0.5)


# 定义为线程方法传入的参数
my_tuple = ("http://c.biancheng.net/python/",
            "http://c.biancheng.net/shell/",
            "http://c.biancheng.net/java/")


# 创建线程
# thread = threading.Thread(target=action, args=my_tuple)

# 创建多线程
for n in range(3):
    thread = threading.Thread(target=action, args=my_tuple)
    thread.start()

# 主线程
for i in range(5):
    print(threading.current_thread().getName())
