"""
2019.11.26 16:45
正则表达式

# 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
re.match(pattern, string, flags=0)
    pattern	匹配的正则表达式
    string	要匹配的字符串。
    flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等
        re.I 忽略大小写
        re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
        re.M 多行模式
        re.S 即为' . '并且包括换行符在内的任意字符（' . '不包括换行符）
        re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
        re.X 为了增加可读性，忽略空格和' # '后面的注释

# 匹配对象函数来获取匹配表达式
group(num=0) 或 groups()

# 扫描整个字符串并返回第一个成功的匹配
re.search(pattern, string, flags=0)

# 替换字符串中的匹配项
re.sub(pattern, repl, string, count=0, flags=0)
    pattern : 正则中的模式字符串。
    repl : 替换的字符串，也可为一个函数。
    string : 要被查找替换的原始字符串。
    count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
    flags : 编译时用的匹配模式，数字形式。

# 编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用
re.compile(pattern[, flags])
    pattern : 一个字符串形式的正则表达式
    flags 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：

# 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表
re.findall(string[, pos[, endpos]])
    string 待匹配的字符串。
    pos 可选参数，指定字符串的起始位置，默认为 0。
    endpos 可选参数，指定字符串的结束位置，默认为字符串的长度。

# 在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回
re.finditer(pattern, string, flags=0)

# 按照能够匹配的子串将字符串分割后返回列表
re.split(pattern, string[, maxsplit=0, flags=0])

"""

# !/usr/bin/python3
import re

line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")

####

line = "Cats are smarter than dogs"

matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
    print("match --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

matchObj = re.search(r'dogs', line, re.M | re.I)
if matchObj:
    print("search --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")
    