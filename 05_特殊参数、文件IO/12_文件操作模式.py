lst = [
    "今天天气不错", 
    "挺风和日丽的",
    "我们下午在上课"
]

# 使用with可以保证即使出现异常，可以关闭文件
with open("c.txt", "a+", encoding="utf8") as f:
    # 通过推导式，给每个元素追加一个\n
    # lst = [ item + "\n" for item in lst ]
    # f.writelines(lst)
    
    # f.seek(3) # 跳到指定字节
    content = f.read()
    print(content)

print("closed: ", f.closed)
