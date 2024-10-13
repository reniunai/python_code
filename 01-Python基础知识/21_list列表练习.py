"""
一个学校，有3个办公室，现在有8位老师等待工位的分配
['袁腾飞', '罗永浩', '俞敏洪', '李永乐', '王芳芳', '马云', '李彦宏', '马化腾']

请编写程序:
1. 完成随机的分配
2. 打印办公室信息 (每个办公室中的人数，及分别是谁)
"""
import random

# 0, 1, 2
house_lst = [[], [], []]

names = ["袁腾飞", "罗永浩", "俞敏洪", "李永乐", "王芳芳", "马云", "李彦宏", "马化腾"]

for name in names:
    # 随机选择一个办公室
    house_id = random.randint(0, 2)

    # 把当前name放进去(提取变量 Ctrl + Shift + R)
    house_lst[house_id].append(name)

print(house_lst)
