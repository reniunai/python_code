"""
输入一个文件名,统计文件中
- 注释行数
- 空行数
- 代码行数 
"""
file_name = input("请输入文件名：")

comment_lines = 0
blank_lines = 0
code_lines = 0

# 读取文件内容
with open(file_name, encoding="UTF-8") as f:
    lines = f.readlines()
    
    # 循环所有lines
    for line in lines:
        line = line.strip()
        if line.startswith("#"):    # 注释
            comment_lines += 1
        elif line == "":
            blank_lines += 1
        else:
            code_lines += 1 
       
print("注释行数：{} 空行数：{} 代码行数: {}".format(comment_lines, blank_lines, code_lines))