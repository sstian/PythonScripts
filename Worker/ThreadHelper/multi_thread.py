"""
python 多线程读取列表（可以设置线程数，平均分配每个线程读取的列表数）
https://junyiseo.com/python/211.html
"""
# -*- coding: UTF-8 -*-
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, thread_id, thread_name, start_pos, end_pos):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.thread_name = thread_name
        self.start_pos = start_pos
        self.end_pos = end_pos

    def run(self):
        print(f"Starting {self.thread_name} at {time.ctime()}")
        # 获得锁，成功获得锁定后返回True
        # 可选的timeout参数不填时将一直阻塞直到获得锁定
        # 否则超时后将返回False
        thread_lock.acquire()
        # 线程需要执行的方法
        print_image(self.thread_name, self.start_pos, self.end_pos)
        # 释放锁
        thread_lock.release()


# 创建需要读取的列表
image_list = []
for i in range(12):
    image_list.append(i)


# 按照分配的区间，读取列表内容
def print_image(thread_name, start_pos, end_pos):
    for index in range(int(start_pos), int(end_pos)):
        print(f"{thread_name}: {index}")


# 需要创建的线程数
total_thread = 3
# 列表的总长度
len_list = len(image_list)
# 列表分配到每个线程的执行数
gap = len_list / total_thread

# 锁
thread_lock = threading.Lock()
# 创建线程列表
threads = []

# 创建新线程和添加线程到列表
for i in range(total_thread):
    thread = "thread%s" % i
    if i == 0:
        thread = MyThread(0, "Thread-%s" % i, 0, gap)
    elif total_thread == i + 1:
        thread = MyThread(i, "Thread-%s" % i, i * gap, len_list)
    else:
        thread = MyThread(i, "Thread-%s" % i, i * gap, (i + 1) * gap)
    # 添加至线程到列表
    threads.append(thread)

# 循环开启线程
for j in range(total_thread):
    threads[j].start()

# 等待所有线程完成
for t in threads:
    t.join()
print("Exit Main Thread")
