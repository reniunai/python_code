lst = [
    "今天天气不错", 
    "挺风和日丽的",
    "我们下午在上课"
]

# 使用with可以保证即使出现异常，可以关闭文件
with open("c.txt", "w", encoding="utf8") as f:
    # 通过推导式，给每个元素追加一个\n
    lst = [ item + "\n" for item in lst ]
    f.writelines(lst)

print("closed: ", f.closed)

# 文件关闭之后不能再读写，否则ValueError: I/O operation on closed file.
# f.write("abc")