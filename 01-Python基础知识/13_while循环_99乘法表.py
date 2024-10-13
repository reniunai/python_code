"""
1. 打印星星
2. 使用嵌套循环打印阶梯星星
3. 将星星替换成乘法口诀公式
"""

print("------------------------------------------------------------------正序乘法表")
row = 1
while row <= 9:
    # 打印每一行内容
    col = 1
    while col <= row:
        print("%d * %d = %d" % (col, row, col * row), end="\t")
        col += 1
        
    print()
    row += 1
    
print("------------------------------------------------------------------倒序乘法表")
row = 9
while row >= 1:
    
    # 打印每一行内容
    col = 1
    while col <= row:
        print("%d * %d = %d" % (col, row, col * row), end="\t")
        col += 1
        
    print()
    
    row -= 1