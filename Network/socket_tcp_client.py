"""
2019.11.27 13:12
Socket TCP Client

客户端结构：
tcpc = socket()    # 创建客户端套接字
tcpc.connect()    # 尝试连接服务器
while True:        # 通讯循环
    tcpc.send()/tcpc.recv()    # 对话(发送/接收)
tcpc.close()      # 关闭客户套接字
"""

# 时间戳客户端实例：

# #!/usr/bin/python3
# -*-coding:utf-8 -*-

from socket import *
from time import ctime

HOST = '127.0.0.1'  # '192.168.164.141' # 服务端ip
PORT = 8010  # 服务端端口号
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)  # 创建socket对象
tcpCliSock.connect(ADDR)  # 连接服务器
while True:
    data = input('>>').strip()
    if not data:
        break
    tcpCliSock.send(data.encode('utf-8'))  # 发送消息
    data = tcpCliSock.recv(BUFSIZE)  # 读取消息
    if not data:
        break
    print(data.decode('utf-8'))
tcpCliSock.close()  # 关闭客户端
