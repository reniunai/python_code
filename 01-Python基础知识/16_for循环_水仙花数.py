"""
1. 遍历所有的三位数
2. 求 百位 十位 个位  立方和
3. 判断并打印
"""

for i in range(100, 1000):
    # 123 -> 12
    baiwei = i // 100
    shiwei = i // 10 % 10
    gewei = i % 10

    if (baiwei**3 + shiwei**3 + gewei**3) == i:
        print("{} + {} + {} = {}".format(baiwei**3, shiwei**3, gewei**3, i))