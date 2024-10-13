"""
需求：
1. 从控制台输入要出的拳 —— 
    石头（1）／剪刀（2）／布（3）
2. 电脑 随机 出拳 —— 先假定电脑只会出石头，完成整体代码功能
3. 比较胜负并输出结果
"""

mine = int(input("出拳: "))

computer = 1 # 石头

if mine == 3 and computer == 1:
    print("我win")
elif mine == computer:
    print("平局tie")
else:
    print("电脑win")