"""可变长度参数"""


def sum_nums(*args):
    print("args1: ", type(args))
    
    rst = 0
    for i in args:
        rst += i

    return rst

def sum_nums1(name, *args):
    print("name: ", name)
    
    rst = 0
    for i in args:
        rst += i

    return rst


# rst = sum_nums(1, 2, 3, 4, 5)
rst = sum_nums1("abc",1, 2, 3, 4, 5)
print(rst)
