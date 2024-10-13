for i in range(10):
    if i == 3:
        break
    print("媳妇, 我错了", i)
else:
    print("顺利完成, 原谅我了")

# else的代码只在正常循环完毕时执行, 出现break则不再执行
print("---------------------------")

for i in range(10):
    if i % 2 == 0:
        continue
    print("媳妇, 我错了", i)
else:
    print("顺利完成, 原谅我了")
