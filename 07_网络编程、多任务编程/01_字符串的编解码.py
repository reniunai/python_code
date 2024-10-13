print("----------------------------------------UTF-8")
# 将字符串转成bytes类型
bytes_arr = "今晚!".encode(encoding="UTF-8") # encoding默认模式utf-8
# b'\xe4\xbb\x8a\xe6\x99\x9a' <class 'bytes'> utf-8, 用3个字节代表一个汉字
print(bytes_arr, type(bytes_arr)) 
str_rst = bytes_arr.decode(encoding="UTF-8")
print(str_rst)

print("----------------------------------------GBK")
bytes_arr = "今晚来吃鸡啊".encode(encoding="GBK") # encoding默认模式utf-8
# b'\xbd\xf1\xcd\xed'   <class 'bytes'> gbk , 用2个字节代表一个汉字
print(bytes_arr, type(bytes_arr)) 
str_rst = bytes_arr.decode(encoding="GBK")
print(str_rst)

print("-----------------------直接声明字节数组")
bytes_arr = b'\xbd\xf1\xcd\xed'
str_rst = bytes_arr.decode(encoding="GBK")
print(str_rst)



