a = 10
b = int(input("输入b: "))

try:
    c = a / b
    print("结果: ", c)
except ZeroDivisionError as e:
    print(e)
    print("除数不能为0")
    
print("------------------------")