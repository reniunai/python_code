"""
打印名片
"""
name = input("姓名: ")
company = input("公司: ")
title = input("职位: ")
telephone = input("电话: ")
email = input("邮箱: ")

print("*" * 30)
print(company)
print()
print("%s (%s)" % (name, title))    # 如果字符串里有多个占位符, %后就写对应个数参数()包裹
print()
print("电话: ", telephone)
print("邮箱: ", email)
print("*" * 30)