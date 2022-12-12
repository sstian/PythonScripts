"""
2019.11.09 15:18 - 15:21
循环控制 continue：某一条件满足时，不执行后续代码
"""
index = 1
while index <= 10:
    if index == 3:
        index += 1
        continue

    print(index)
    index += 1
