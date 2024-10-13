import sys

# 命令行启动参数
print(sys.argv)
print(sys.argv[1:])
print(sys.path)
# sys.exit(0)

print("-------------------------------- time")
import time

start = time.time()  # 时间戳, 单位s, 1970.1.1到现在秒数
# 阻塞当前线程， 单位s
# time.sleep(2)
end = time.time()

print(f"duration: {end - start}")

print("------------------------------- datetime")
from datetime import datetime

now = datetime.now()
print(now, type(now))
print(now.year, now.month, now.day, now.hour, now.minute, now.second)
# 直接把now对象，转成目标时间日期格式
print(datetime.strftime(now, "%Y-%m-%d %H:%M:%S"))
date_str = "2023_10_09 10|11|12"
parse_rst = datetime.strptime(date_str, "%Y_%m_%d %H|%M|%S")
print(parse_rst)

print("--------------------------------- list")

arr = [2, 3, 5, 1, 12, 7, 8, 4]
print(max(arr))
print(min(arr))
print(len(arr))
print(sum(arr))
print(type(arr))
# arr.sort()            # 会修改原始数据
# new_arr = sorted(arr)   # 会得到一个新的列表，不会修改原始数据
new_arr = sorted(arr, reverse=True)   # 会得到一个新的列表，不会修改原始数据

print(arr)
print(new_arr)
