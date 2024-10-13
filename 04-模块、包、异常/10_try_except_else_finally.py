a = 10
b = 0
try:
    result = a / b
    print(f"1.result: {result}")
except:
    print('2.出异常')
else:
    print('3.没有出异常')
finally:
    print('4.最终执行的代码')