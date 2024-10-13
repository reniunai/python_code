"""
● 用户名和密码格式校验程序
● 要求从键盘输入用户名和密码，分别校验格式是否符合规则
  ○ 如果符合，打印用户名合法，密码合法
  ○ 如果不符合，打印出不符合的原因，并提示重新输入
  
● 用户名长度6-20，用户名必须以字母开头
● 密码长度至少6位，不能为纯数字，不能有空格
"""

while True:  # 循环获取用户输入，符合要求，退出循环，否则一直循环
    username = input("请输入用户名：")
    # 用户名长度6-20，用户名必须以字母开头
    if len(username) < 6 or len(username) > 20:
        print("用户名长度不符合要求")
    elif not username[0].isalpha():
        print("用户名必须以字母开头")
    else:
        print("用户名合法")
        break

print("username: ", username)

while True:
    password = input("请输入密码：")
    # 密码长度至少6位，不能为纯数字，不能有空格
    if len(password) < 6:
        print("密码长度不符合要求")
        continue

    if password.isdecimal():
        print("密码不能为纯数字")
        continue

    if " " in password:
        print("密码不能有空格")
        continue

    print("密码合法")
    break
