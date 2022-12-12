"""
2019.11.24 01:06
包

正在发送 hello
收到 100xx 的消息
"""


import hm_message

hm_message.send_message.send("hello")

recv = hm_message.receive_message.receive()
print(recv)
