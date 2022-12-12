"""
2019.11.27 16:11
JSON=JavaScript Object Notation 数据解析
    一种轻量级的数据交换格式。它基于ECMAScript的一个子集

Python 编码为 JSON 类型转换对应表：
dict	        object
list, tuple	    array
str	            string
int, float  	number
True	        true
False	        false
None	        null

JSON 解码为 Python 类型转换对应表：
number (int)	int
number (real)	float
……

Python 原始数据： {'no': 1, 'name': 'Runoob', 'url': 'http://www.runoob.com'}
JSON 对象： {"no": 1, "name": "Runoob", "url": "http://www.runoob.com"}
"""

# #!/usr/bin/python3

import json

# Python 字典类型转换为 JSON 对象
data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

json_str = json.dumps(data)
print("Python 原始数据：", repr(data))
print("JSON 对象：", json_str)


# 写入 JSON 数据文件
with open('data.json', 'w') as f:
    json.dump(data, f)
