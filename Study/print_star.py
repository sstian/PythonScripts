"""
2019.11.09 15:28 - 15:30
打印星星
*
**
***
****
*****
"""

import def_function

row = 1

# 控制行
while row <= 5:

    # 控制列
    col = 1
    while col <= row:
        # 去掉默认换行
        print("*", end="")
        col += 1

    #换行
    print()
    row += 1

result = def_function.sum(12, 13)
print("sum = %d" % result)


