"""
开启线程：Thread-1
开启线程：Thread-2
开启线程：Thread-3
Thread-3 processing One
Thread-2 processing Two
Thread-1 processing Three
Thread-3 processing Four
Thread-2 processing Five
退出线程：Thread-1
退出线程：Thread-3
退出线程：Thread-2
退出主线程
"""

# #!/usr/bin/python3

import queue
import threading
import time

exit_flag = 0


class MyThread (threading.Thread):
    def __init__(self, thread_id, name, q):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
        self.q = q

    def run(self):
        print ("开启线程：" + self.name)
        process_data(self.name, self.q)
        print ("退出线程：" + self.name)


def process_data(thread_name, q):
    while not exit_flag:
        queue_lock.acquire()
        if not work_queue.empty():
            data = q.get()
            print ("%s processing %s" % (thread_name, data))
        queue_lock.release()
        time.sleep(1)


thread_list = ["Thread-1", "Thread-2", "Thread-3"]
name_list = ["One", "Two", "Three", "Four", "Five"]
queue_lock = threading.Lock()
work_queue = queue.Queue(10)
threads = []
thread_id = 1

# 创建新线程
for tName in thread_list:
    thread = MyThread(thread_id, tName, work_queue)
    thread.start()
    threads.append(thread)
    thread_id += 1

# 填充队列
queue_lock.acquire()
for word in name_list:
    work_queue.put(word)
queue_lock.release()

# 等待队列清空
while not work_queue.empty():
    pass

# 通知线程是时候退出
exit_flag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")
