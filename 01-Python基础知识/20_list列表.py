# 列表初始化
name_list = ["樱木花道", "佐助", "卡卡西", 12.23, "纲手"]

# 添加元素 Create
name_list.append("自来也")
name_list.append("柯南")

print(name_list)

# 移除元素 Delete
name_list.remove("佐助")
print(name_list)
# name_list.remove("鸣人")    # 移除不存在的元素，会报异常，下方的代码不再执行
print(name_list.pop(1)) # 移除指定索引的数据，并返回内容
print(name_list)

# 修改元素 Update
name_list[0] = "流川枫123"

# 查询 R Retrieve
print("-----------------------列表查询")
print(name_list[3])
print(name_list.index("自来也"))
for name in name_list:
    print(name)

print("-----------------------列表的排序")
lst = [2 ,5, 1, 3, 22, 12]
lst.sort()  # 排序
lst.sort(reverse=True)  # 倒序
print(lst)

print("-----------------------列表的嵌套")
students = [
    ['林青霞', "郑少秋", "刘德华"],
    ["张曼玉", "梁朝伟"]
]
print(students[0][1])
print(students[0][2])
print(students[1][6]) # IndexError: list index out of range