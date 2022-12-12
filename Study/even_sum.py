"""
2019.11.09 15:00 - 15:09
偶数求和
"""

result = 0
index = 1

while index <= 100:
    if index % 2 == 0:
        print(index)
        result += index
    index += 1

print("even sum = %d" % result)
