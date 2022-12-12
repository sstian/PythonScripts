"""
2019.11.23 14:50
类属性 类方法
"""

class Tool(object):

    # 类属性
    count = 0

    @classmethod
    def show_tool_count(cls):
        # print("工具总数 %d" % Tool.count)
        print("工具总数 %d" % cls.count)

    def __init__(self, name):
        self.name = name

        Tool.count += 1

tool1 = Tool("水桶")
tool2 = Tool("铁锨")
tool3 = Tool("斧头")

Tool.show_tool_count()

print(tool3.count)
print(Tool.count)

Tool.count = 10
print(Tool.count)
print(tool3.count)

tool3.count = 99
print(Tool.count)
print(tool3.count)

