ages = {
    # key: value键值对
    "Tom": 18,
    "Jack": 19,
    "Rose": 17,
}

# --------------------------------------------------------- 1
# 直接遍历
for key in ages:
    print(key, ages[key])
    
print("--------------------------", type(ages.keys()))
# 获取所有key，遍历
for key in ages.keys():
    print(key, ages[key])
    
print("--------------------------", type(ages.values()))
# 获取所有value，遍历
for value in ages.values():
    print(value)
    
print("--------------------------", type(ages.items()))
# 获取所有键值对
for item in ages.items():
    print(item, type(item))
    
# --------------------------------------------------------- 2
for key, value in ages.items():
    print(key, value)
    
print("创建空的集合和字典， 默认{}是一个字典")
ss = set()
di = dict()
print(ss, type(ss))
print(di, type(di))