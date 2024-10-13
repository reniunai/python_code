def say_hello():
    """
    打招呼函数
    """
    print("Hello World!")
    print("Hello World!")
    print("Hello World!")
    
def sum(a, b):
    """求两个数之和

    :param a: 参数1
    :param b: 参数2
    :return: 两个数之和
    """
    return a + b

def my_max(a, b):
    """返回两个数较大那个

    :param a: _description_
    :param b: _description_
    :return: 较大值
    """
    if a > b:
        return a

    return b

def calc(a, b):
    """计算两个数的乘积和商

    :param a: _description_
    :param b: _description_
    :return: 结果的元组
    """
    
    # 两个数乘积
    multiply = a * b
    
    if b == 0:
        return multiply, None
    # 两个数的商
    divide = a / b
    
    return multiply, divide # 返回多个值，自动组包成元组tuple

say_hello()
print(sum(3, 5))
print(my_max(21, 100))

print(calc(3, 7))

x, y = calc(3, 0)
print(x, y)