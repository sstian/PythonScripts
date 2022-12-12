"""
2019.11.27 16:29
时间日期

struct_time 时间元组：
序号	属性	字段          值
0	tm_year     4位数年       2008
1	tm_mon	    月           1 到 12
2	tm_mday	    日           1 到 31
3	tm_hour	    小时         0 到 23
4	tm_min	    分钟         0 到 59
5	tm_sec	    秒           0 到 61 (60或61 是闰秒)
6	tm_wday	    一周的第几日  0到6 (0是周一)
7	tm_yday	    一年的第几日  1 到 366
8	tm_isdst    夏令时	    是否为夏令时，值有：1(夏令时)、0(不是夏令时)、-1(未知)，默认 -1

python中时间日期格式化符号：
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称  # 乱码
%% %号本身

[1]
1574845252.24516
[2]
time.struct_time(tm_year=2019, tm_mon=11, tm_mday=27, tm_hour=17, tm_min=0, tm_sec=52, tm_wday=2, tm_yday=331, tm_isdst=0)
time.struct_time(tm_year=2019, tm_mon=11, tm_mday=27, tm_hour=16, tm_min=45, tm_sec=17, tm_wday=2, tm_yday=331, tm_isdst=0)
[3]
Wed Nov 27 17:00:52 2019
Wed Nov 27 16:45:17 2019
[4]
1574844317.0
[5]
Wed Nov 27 17:00:52 2019
Wed Nov 27 16:45:17 2019
Wed Nov 27 16:45:17 2019
[6]
2019-11-27 17:00:52
[7]
time.struct_time(tm_year=2019, tm_mon=11, tm_mday=27, tm_hour=16, tm_min=57, tm_sec=34, tm_wday=2, tm_yday=331, tm_isdst=-1)
[8]
0.0811479
0.09375
以下输出2016年1月份的日历:
   November 2019
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30

"""

# #!/usr/bin/python

import time
import calendar


# （1）当前时间戳
# 1574844317.5947008
print("[1]")
print(time.time())

# （2）时间戳 → 时间元组
# time.localtime(时间戳)，默认为当前时间
# time.struct_time(tm_year=2018, tm_mon=9, tm_mday=3, tm_hour=9, tm_min=4, tm_sec=1, tm_wday=6, tm_yday=246, tm_isdst=0)
print("[2]")
print(time.localtime())
print(time.localtime(1574844317.5947008))

# （3）时间戳 → 可视化时间
# time.ctime(时间戳)，默认为当前时间
# Wed Nov 27 16:45:17 2019
print("[3]")
print(time.ctime())
print(time.ctime(1574844317.5947008))

# （4）时间元组 → 时间戳
# 1574844317.0
print("[4]")
print(time.mktime((2019, 11, 27, 16, 45, 17, 2, 331, 0)))

# （5）时间元组 → 可视化时间
# time.asctime(时间元组)，默认为当前时间
# Wed Nov 27 16:55:52 2019
print("[5]")
print(time.asctime())
print(time.asctime((2019, 11, 27, 16, 45, 17, 2, 331, 0)))
print(time.asctime(time.localtime(1574844317.5947008)))

# （6）时间元组 → 可视化时间（定制）
# time.strftime(要转换成的格式，时间元组)
print("[6]")
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# （7）可视化时间（定制） → 时间元祖
# time.strptime(时间字符串，时间格式)
print("[7]")
print(time.strptime('2019-11-27 16:57:34', '%Y-%m-%d %H:%M:%S'))

# （8）浮点数秒数，用于衡量不同程序的耗时，前后两次调用的时间差
print("[8]")
print(time.perf_counter())  # 返回系统运行时间
print(time.process_time())  # 返回进程运行时间


# 日历
# 星期一是默认的每周第一天，星期天是默认的最后一天。更改设置需调用calendar.setfirstweekday()函数
cal = calendar.month(2019, 11)
print ("以下输出2016年1月份的日历:")
print (cal)

