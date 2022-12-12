"""
{'no': 1, 'name': 'Runoob', 'url': 'http://www.runoob.com'}
data['name']:  Runoob
data['url']:  http://www.runoob.com
"""

# !/usr/bin/python3

import json


# 读取 JSON 数据文件
with open('data.json', 'r') as f:
    data = json.load(f)
print(data)
print ("data['name']: ", data['name'])
print ("data['url']: ", data['url'])


# # 定义 Python 字典
# data1 = {
#     'no': 1,
#     'name': 'Runoob',
#     'url': 'http://www.runoob.com'
# }
#
# # 将 Python 字典类型转换为 JSON 对象
# json_str = json.dumps(data1)
#
# # 将 JSON 对象转换为 Python 字典
# data2 = json.loads(json_str)
# print("data2['name']: ", data2['name'])
# print("data2['url']: ", data2['url'])


