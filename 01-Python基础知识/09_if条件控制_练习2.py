"""
需求：
1. 从控制台输入要出的拳 —— 
    石头（1）／剪刀（2）／布（3）
2. 电脑 随机 出拳 —— 先假定电脑只会出石头，完成整体代码功能
3. 比较胜负并输出结果
"""
import random

mine = int(input("出拳: "))

computer = random.randint(1, 3)

if (mine == 3 and computer == 1) or (mine == 1 and computer == 2) or (mine == 2 and computer == 3):
    print("我win: mine: %d -> computer: %d" % (mine, computer))
elif mine == computer:
    print("平局tie: mine: %d -> computer: %d" % (mine, computer))
else:
    print("电脑win: mine: %d -> computer: %d" % (mine, computer))