"""
需求
完成字符串的逆序以及统计
设计一个程序，要求只能输入长度低于31的字符串，否则提示用户重新输入
打印如下内容:
--------------------------------------------
您输入的字符串: zhongshanshan
长度: 13
逆序后为: nahsnahsgnohz
字符统计结果: z:1 h:3 o:1 n:3 g:1 s:2 a:2
--------------------------------------------
"""


template = """--------------------------------------------
您输入的字符串: {}
长度: {}
逆序后为: {}
字符统计结果: {}
--------------------------------------------
"""
# zhangshanshan
# 接受用户输入的字符串 < 31
while True:
    ss = input("请输入字符串：")
    if len(ss) < 31:
        break
    else:
        print("长度必须小于31：", len(ss))
        
print(ss)

# 统计每一个字符对应出现的次数 zhongshanshan
stat_dict = {"z": 0, "s": 0}
# 循环遍历字符串的每个字符
for s in ss:
    if s not in stat_dict:
        # 不在字典，初始化为1
        stat_dict[s] = 1
    else:
        # 之前存过， 取出来+1放回去
        stat_dict[s] += 1

# 字典转成列表
output_lst = ["{}:{}".format(k,v) for k, v in stat_dict.items()]
# print(output_lst)
# print(" ".join(output_lst)) # join和split互为反向操作

# 统计并输出
print(template.format(
    ss,
    len(ss),
    ss[::-1],
    " ".join(output_lst)    # 用空格分隔列表的每个元素，合并成一个完整的字符串
))