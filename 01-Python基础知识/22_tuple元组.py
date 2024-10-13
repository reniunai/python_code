names = ("柯南",) #tuple 如果只有一个元素，记得加上,

names = ("柯南", "小五郎", "毛利兰")
print(names, type(names))

# 自动组包tuple
names = "柯南", "毛利兰"
print(names, type(names))

# 自动解包 unpack
name1, name2 = names
print(name1, name2)

stu = "张干饭", 26, 175.5
name, age, height = stu
print("name: {}, age: {}, height: {}".format(name, age, height))

print("-----------------------------------数据交换")
a = 4
b = 7
temp = a
a = b
b = temp
print(a, b)

a = 3
b = 2
b, a = a, b
print(a, b)

print("---------------------------------内容不可修改")
names = ("柯南", "小五郎", "毛利兰")    # 元组内容不可修改
names_lst = list(names)                # 如果需要修改，转成list

names = ['袁腾飞', '罗永浩', '俞敏洪', '李永乐', '王芳芳', '马云', '李彦宏', '马化腾']
names_tuple = tuple(names)              # 将list转成不可修改的tuple
# names_tuple[1] = "老罗" 
# print("aaa")
print(names_tuple[4])
# for name in names_tuple:
#     print(name)