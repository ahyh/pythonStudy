card_list = []


def show_menu():
    print("*" * 50)
    print("欢迎使用文件管理系统")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("")
    print("0.退出系统")
    print("*" * 50)


def add_card():
    """
    新增名片
    :return:
    """
    print("-" * 50)
    print("新增名片")
    # 提示用户输入名片信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ：")
    email_str = input("请输入email：")

    # 使用用户输入的信息新建一个名片的信息
    card_dict = {"name": name_str, "phone": phone_str, "qq": qq_str, "email": email_str}

    # 将名片字典加入到列表中
    card_list.append(card_dict)
    print(card_list)
    print("添加%s的名片成功" % name_str)


def show_all():
    """
    展示名片
    :return:
    """
    print("-" * 50)
    print("展示名片")
    if len(card_list) == 0:
        print("当前列表中没有名片，请先操作添加名片")
        return
    # 遍历列表展示名片信息
    for name in ["姓名", "电话", "qq", "邮箱"]:
        print(name, end="\t\t")
    print("")
    print("*" * 50)
    for card in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card["name"], card["phone"], card["qq"], card["email"]))
    print("*" * 50)


def search_card():
    """
    修改名片
    :return:
    """
    print("-" * 50)
    print("搜索名片")
    # 提示用户输入要搜索的姓名
    search_name = input("请输入要搜索的姓名")
    # 遍历名片列表，查询要搜索的姓名，如果没有的话提示未找到
    for card in card_list:
        if search_name == card["name"]:
            for name in ["姓名", "电话", "qq", "邮箱"]:
                print(name, end="\t\t")
            print("")
            print("*" * 50)
            print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card["name"], card["phone"], card["qq"], card["email"]))
            print("*" * 50)
            deal_card(card)
            break
    else:
        print("没有找到%s的名片" % search_name)


def deal_card(card):
    deal_str = input("请选择要执行的操作："
                     "【1】-修改 【2】-删除 【0】-返回上级菜单")
    if deal_str == "1":
        card["name"] = input_card_info(card["name"], "姓名：")
        card["phone"] = input_card_info(card["phone"], "电话号码：")
        card["qq"] = input_card_info(card["qq"], "QQ：")
        card["email"] = input_card_info(card["email"], "邮箱：")
        print("修改名片成功")
    elif deal_str == "2":
        card_list.remove(card)
        print("删除名片成功!")


def input_card_info(dict_value, tip_message):
    """

    :param dict_value:字典中原有的值
    :param tip_message:输入的提示文字信息
    :return:如果用户输入了需要修改后的值就返回，否则返回原有的值  
    """
    # 提示用户输入内容
    input_str = input(tip_message)
    if len(input_str) > 0:
        return input_str
    else:
        return dict_value
