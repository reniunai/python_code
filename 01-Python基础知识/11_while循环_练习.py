"""根据用户输入的数值n，打印n行三角形"""

n = int(input("请输入行数: "))

# 正三角
# row = 1
# while row <= n:
#     print("*" * row)
#     row += 1

# 倒三角
row = n # 5, 4, 3, 2, 1
while row >= 1:
    print('*' * row)
    row -= 1