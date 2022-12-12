"""
2019.11.27 13:08
Socket TCP Server

服务端结构：
tcps = socket() #创建服务器套接字
tcps.bind()      #把地址绑定到套接字
tcps.listen()      #监听链接
while True:      #服务器无限循环
    tcpc = tcps.accept() #接受客户端链接
    while True:         #通讯循环
        tcpc.recv()/tcpc.send() #对话(接收与发送)
    tcpc.close()    #关闭客户端套接字
tcps.close()        #关闭服务器套接字(可选)
"""


# 时间戳服务端实例：

# #!/usr/bin/python3
# -*-coding:utf-8 -*-

from socket import *
import time

COD = 'utf-8'
HOST = '127.0.0.1'  # '192.168.164.141' # 主机ip
PORT = 8010  # 软件端口号
BUFSIZE = 1024
ADDR = (HOST, PORT)
SIZE = 10

tcpS = socket(AF_INET, SOCK_STREAM)  # 创建socket对象
tcpS.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)  # 加入socket配置，重用ip和端口
tcpS.bind(ADDR)  # 绑定ip端口号
tcpS.listen(SIZE)  # 设置最大链接数
while True:
    print("服务器启动，监听客户端链接")
    conn, addr = tcpS.accept()
    print("链接的客户端", addr)
    while True:
        try:
            data = conn.recv(BUFSIZE)  # 读取已链接客户的发送的消息
        except Exception:
            print("断开的客户端", addr)
            break
        print("客户端发送的内容:",data.decode(COD))
        if not data:
            break
        msg = time.strftime("%Y-%m-%d %X")  # 获取结构化时间戳
        msg1 = '[%s]:%s' % (msg, data.decode(COD))
        conn.send(msg1.encode(COD))  # 发送消息给已链接客户端
    conn.close()  # 关闭客户端链接
tcpS.close()
