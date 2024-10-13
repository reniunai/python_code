ss = {"孙悟空", "猪八戒", "唐僧", "沙和尚", "孙悟空"}
print(ss)

for ele in ss:
    print(ele)
    
ss.add("白骨精")

ss.remove("唐僧")
# 安全移除, 若条目不存在，不抛出异常
ss.discard("牛魔王")

print("------------------pop")
# 随机移除元素
print(ss.pop())

print(ss)
# 清空
ss.clear()
print(ss)