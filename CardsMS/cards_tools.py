
# 记录所有的名片字典列表
card_list = [{"name": "ayu",
              "phone": "15732136885",
              "qq": "1344081234",
              "email": "ming@qq.com"},
             {"name": "mei",
              "phone": "15610041478",
              "qq": "348434258",
              "email": "mei@163.com"}
             ]


def show_menu():
    """显示主菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】 V1.0")
    print("")
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)


def new_card():
    """新增名片"""
    print("-" * 50)
    print("新增名片")

    # 1. 提示用户输入名片的详细信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ：")
    email_str = input("请输入邮箱：")

    # 2. 使用用户输入的信息建立一个名片字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}

    # 3. 将名片字典添加到列表中
    card_list.append(card_dict)
    # print(card_list)

    # 4. 提示用户添加成功
    print("添加 %s 的名片成功！" % name_str)


def show_all():
    """显示全部名片"""
    print("-" * 50)
    print("显示全部名片")

    # 判断是否存在名片记录，没有则返回
    if len(card_list) == 0:
        print("当前没有任何名片记录，请使用新增功能添加")
        return

    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")

    print("")

    # 打印分割线
    print("=" * 50)

    # 遍历名片列表依次输入字典信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))


def search_card():
    """查询名片"""
    print("-" * 50)
    print("查询名片")

    # 1. 提示输入
    find_name = input("请输入要查询的姓名：")

    # 2. 遍历
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                                card_dict["phone"],
                                                card_dict["qq"],
                                                card_dict["email"]))

           # 对找到的记录修改或删除
            deal_card(card_dict)

            break

    else:
        print("抱歉，没有找到 %s" % find_name)


def deal_card(find_dict):
    """处理查找到的名片

    :param find_dict: 查找到的名片
    :return: 无
    """
    # print(find_dict)

    action_str = input("请选择要执行的操作 "
                       "[1]修改 [2]删除 [0]返回上级菜单")
    if "1" == action_str:
        find_dict["name"] = input_card_info(find_dict["name"], "姓名[按回车不修改]：")
        find_dict["phone"] = input_card_info( find_dict["phone"], "电话[按回车不修改]：")
        find_dict["qq"] = input_card_info( find_dict["qq"], "QQ[按回车不修改]：")
        find_dict["email"] = input_card_info( find_dict["email"], "邮箱[按回车不修改]：")
        print("修改名片成功！")

    elif "2" == action_str:
        card_list.remove(find_dict)
        print("删除名片成功！")


def input_card_info(dict_value, tip_message):
    """输入名片信息

    :param dict_value: 字典中原有的值
    :param tip_message: 输入的提示文字
    :return: 输入了内容，返回内容，否则，返回字典中原有的值
    """
    # 1. 提示用户输入
    result_str = input(tip_message)

    # 2. 对输入判断
    if len(result_str) > 0:
        return result_str

    # 3. 没有输入，返回‘字典中原有的值’
    else:
        return dict_value
