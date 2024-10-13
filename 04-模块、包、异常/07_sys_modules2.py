import math
# 幂
print(math.pow(10, 2))
# 向下取整1.832156
print(math.floor(1.832156))
print(math.floor(1.123443))
# 向上取整
print(math.ceil(1.832156))
print(math.ceil(1.123443))
# 四舍五入
print(round(1.832156))  # 2
print(round(1.123443))  # 1

# sin 30, 45, 60 参数是弧度 PI -> π/6 -> 30/180
print(math.pi)
print(math.sin(math.pi / 6))

print("-------------------------------random")

import random

# 随机整数 [a, b], including both end points
print(random.randint(10, 20))
# 随机小数 [0,1)
print(random.random())
# 随即浮点类型
print(random.uniform(1.3, 8.4))

# 从列表中随机获取元素
arr = ["张三", "李四", "王五", "赵六", "田七", "刘备"]
print(random.choice(arr))

# 随即返回一个列表，只有一个元素
print(random.choices(arr))
