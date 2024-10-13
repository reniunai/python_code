"""
变量定义, 基本数据类型
"""
# 字符串类型 str
name = "张三"
# 整数类型 int
age = 18
# 浮点类型 float
height = 180.5
# 布尔类型 bool
handsome = True
# 复数 complex
compl = -3+4j

print("height: ", height, " age: ", age)
print(type(name))
print(type(height))
print(type(age))

print(" ----------------------------------")
""" 非法变量名
1. 只能由数字、字母、_(下划线)组成
2. 不能以数字开头
3. 不能是关键字
4. 区分大小写
"""
# abc& = 123
# abc-89757 = 123
# 41abc = 123
# for = "aaa"
user_name = "zhang"
userName  = "san"
USERNAME  = "feng"
print(userName)
print(USERNAME)

print("-------------------------------")
a = 5
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)    # 得到float
print(a // b)   # 整除
print(a % b)    # 取模（求余数）
print(a ** b)   # a ^ b a的b次幂
print("------------------------------")

pwd = "abc123"
# 字符串直接通过+拼接
print(user_name + pwd)
# 字符串可以和数字相乘，重复a次
print(user_name * a)

print("-" * 50)

