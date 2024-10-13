"""
1 2 3
1 2 3
1 2 3
1 2 3
1 2 3
"""

row = 0
while row < 5:
    # 打印每一行的内容
    col = 1
    while col <= 3:
        print(col, end=" ")
        col += 1
        
    # 打印换行
    print()
    
    row += 1