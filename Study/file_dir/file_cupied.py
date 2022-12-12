"""
2019.11.24 23:20 - 23:24
文件复制
"""

# 打开
file_read = open("readme.txt")
file_write = open("readme[cupied].txt", "w")

# 读、写
while True:
    text = file_read.readline()
    if not text:
        break

    file_write.write(text)

#关闭
file_read.close()
file_write.close()
