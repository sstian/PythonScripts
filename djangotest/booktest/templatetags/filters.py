# 自定义过滤器
# 1) 导包
from django import template

# 2) 创建Library对象
register = template.Library()

# 3) 自定义过滤器函数并被装饰
@register.filter
# @library.filter(name="num")
def mod(num):
    """ 判断num是否为偶数"""
    return num % 2 == 0

@register.filter
def mod_val(num, val):
    """ 判断num是否能被val整除"""
    return num % val == 0
