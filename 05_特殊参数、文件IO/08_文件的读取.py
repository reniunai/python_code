# 1. 打开文件 (默认使用系统编码：Window:GBK, Linux/Mac:UTF-8)
f = open("a.txt", mode="r", encoding="UTF-8")
# 2. 读取内容
content = f.read()
print(content)
# 3. 关闭文件
f.close()