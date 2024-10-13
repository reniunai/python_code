# file_path = "D:\\Python\\Lessons\\Code\\05_特殊参数、文件IO\\12_文件操作模式.py"
# 绝对路径
file_path = "D:/Python/Lessons/Code/05_特殊参数、文件IO/12_文件操作模式.py"
print(file_path)
with open(file_path, encoding="utf-8") as f:
    print(f.read())
    
    
# 相对路径
# ./  代表当前目录，可以省略
# ../ 代表上一级目录
with open("../test/test_time.py", encoding="utf8") as f:
    print(f.read())