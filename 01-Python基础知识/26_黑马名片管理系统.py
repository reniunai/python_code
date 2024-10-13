"""
1. 程序启动，显示名片管理系统欢迎界面，并显示功能菜单
2. 用户用数字选择不同的功能：新建名片、显示名片、查询名片、退出系统
  a. 用户名片需要记录用户的 姓名、电话、QQ、邮件
  b. 显示名片可以列举出所有已经保存的名片
  c. 如果查询到指定的名片，用户可以选择 修改、删除 名片
"""

main_tip = """**********************************
欢迎使用【名片管理系统】V1.0

1. 新建名片
2. 显示全部
3. 查询名片

0. 退出系统
**********************************
"""
card_list = [
    ["张飒", 13233334444, 123456, "123@qq.com"],
    ["李四", 13244444444, 444, "44@qq.com"]
]

def create_card():
    """新建名片，并加入cards列表
    """
    print("新建名片")
    name = input("请输入姓名：")
    phone = int(input("请输入电话："))
    qq = int(input("请输入qq："))
    email = input("请输入邮箱：")
    
    card = [name, phone, qq, email]
    card_list.append(card)
    print("添加【{}】名片成功".format(name))
    
def show_all():
    """查询所有名片
    """
    print("显示全部")
    print("姓名\t 电话\t\t qq\t\t 邮箱")
    for card in card_list:
        print("{}\t {}\t\t {}\t\t {}".format(card[0], card[1], card[2], card[3]))

def modify_card(card):
    """修改名片
    """
    card[0] = input("请输入用户名：")
    card[1] = int(input("请输入电话："))
    card[2] = int(input("请输入qq："))
    card[3] = input("请输入email：")
    

def handle_card(card):
    """对指定名片进行操作
    如果查询到某个人，可进行如下操作：
    1. 修改
    2. 删除
    0. 返回
    """
    while True:
        action = input("请输入对名片的操作：1.修改 / 2.删除/ 0.返回：")
        if action == "1": # 修改
            print("修改")
            modify_card(card)
            break
        elif action == "2": # 删除
            print("删除")
            card_list.remove(card)
            break
        elif action == "0": 
            break
        else:
            print("输入错误，请重新输入")
        

def query_card():
    """根据用户输入的姓名进行匹配查询
    """
    query_name = input("请输入要查询的姓名：")
    for card in card_list:
        if query_name == card[0]:
            print("找到了： ", card)
            handle_card(card)
            break
    else:
        print("没有找到【{}】".format(query_name))
    

while True:
    print(main_tip)

    action = input("请输入操作：")

    if action == "1":
        create_card()
    elif action == "2":
        show_all()
    elif action == "3":
        query_card()
    elif action == "0":
        print("退出系统")
        # break
        exit(0)
    else:
        print("输入错误，请重新输入！")
