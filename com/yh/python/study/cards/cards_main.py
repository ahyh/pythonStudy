import cards_tools

# 无限循环
while True:
    cards_tools.show_menu()
    input_str = input("请选择您希望执行的操作：")
    print("您选择的操作是【%s】" % input_str)

    # 输入的1,2,3有对应的操作，0退出系统
    if input_str in ["1", "2", "3"]:
        if input_str == "1":
            cards_tools.add_card()
        elif input_str == "2":
            cards_tools.show_all()
        else:
            cards_tools.search_card()
    elif input_str == "0":
        print("欢迎再次使用名片系统")
        break
    else:
        print("您输入的不正确，请重新输入")