# 1. 打开文件 (默认使用系统编码：Window:GBK, Linux/Mac:UTF-8)
f = open("a.txt", encoding="UTF-8")
# 2. 读取内容(指定读取的字符个数)
content = f.read(3) # 会跨行读取
print(content)

# 读取一行
line = f.readline()
print(line)

result = f.readline(15) # 只读当前行内容的指定个数字符
print("readline(6):", result)

# 一次性读取多行
lines = f.readlines()
print(lines)

# 3. 关闭文件
f.close()