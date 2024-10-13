"""
判断登录密码hhew2383dW_fkf&E@^是否合法。
1. 密码必须是数字、字母(大小写都可以)、和下划线，否则不合法
2. 如果密码合法,就输出"密码合法"
"""
password = input("请输入密码: ")

# 1. 定义容器，保存所有的 数字 字母 _
container = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'

# 2. for循环遍历密码中每一个元素
for ele in password:
    # 3. 判断每一个元素是否合法, 如果不合法，执行break
    if ele not in container:
        print("密码不合法, 包含非法字符: ", ele)
        break
else:
    # 4. 合法, 打印密码合法 (没有执行break时, 此代码才执行)
    print("密码合法:", password)