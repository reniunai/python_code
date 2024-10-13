ages = {
    # key: value键值对, Key不可以重复，Value可以
    "Tom": 18,
    "Jack": 18,
    "Rose": 17,
}

print(ages, type(ages))

print("----------------增删改查")
# 添加
ages["张三"] = 33
ages.setdefault("李四", 14)

# 删除
ages.pop("Jack")
del ages["Rose"]    # python2.0+

# 修改
ages["Tom"] = 23
print(ages["Tom"])

ages.clear()