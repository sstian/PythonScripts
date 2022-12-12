"""
2019.11.22 00:05 - 01:32
名片管理系统 Cards Management System
"""

# #! /usr/bin/python3

import cards_tools

while True:
    # 显示功能菜单
    cards_tools.show_menu()

    action_str = input("请选择操作功能 ")
    print("您选择的操作是[%s]" % action_str)

    # 1,2,3 针对名片的操作
    if action_str in ["1", "2", "3"]:

        # 新建名片
        if "1" == action_str:
           cards_tools.new_card()

        # 显示全部
        elif "2" == action_str:
            cards_tools.show_all()

        # 查询名片
        elif "3" == action_str:
            cards_tools.search_card()

    elif "0" == action_str:
        print("欢迎再次使用【名片管理系统】")
        break
    else:
        print("输入错误，请重新输入")

    # pass占位符，保证程序结构完整性
    # pass