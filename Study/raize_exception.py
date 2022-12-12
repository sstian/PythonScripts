"""
2019.11.23 16:45
异常
"""

# def input_password():
#     pwd = input("请输入密码：")
#
#     if len(pwd) >= 8:
#         return
#
#     # 主动抛出异常
#     ex = Exception("异常-密码长度不够")
#     raise ex
#
#
# try:
#     input_password()
# except Exception as result:
#     print("hhh %s" % result)

print("-" * 50)


try:
    num = int(input("请输入一个整数："))
    num = 8 / num
except ValueError:
    print("invalid literal for int() with base 10")
except Exception as result:
    print("%s" % result)
else:
    print("啊哈~没有错")
finally:
    print("完了，撒花")


