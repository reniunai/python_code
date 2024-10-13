"""
计算n的阶乘

5!

5 * 4!

5 * 4 * 3!
...
5 * 4 * 3 * 2 * 1 = 5!
"""

def calc(n):
    """通过递归函数计算一个数的阶乘
    """
    if n == 1:
        return 1
    
    return n * calc(n - 1)
    
print(calc(5))