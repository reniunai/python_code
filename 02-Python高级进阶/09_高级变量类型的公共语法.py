"""
字符串、列表、元组
"""
arr = [1, 2, 3, 6, 5, 4]

print(len(arr))

print(sum(arr))

# 删除元素
del arr[2]

print(arr)

print("max:", max(arr))
print("min:", min(arr))

print(3 in arr)
print(5 in arr)

arr2 = ["a", "b", 3.14]

print(arr + arr2)

print(arr2 * 3)

arr3 = [1, 5, 3]
arr4 = [1, 2, 100]

print(arr3 > arr4)
