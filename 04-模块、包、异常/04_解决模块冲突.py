# from 导入的内容，以后导入为准（覆盖先导入的变量）

# 1. 通过给变量、函数、类 通过as起别名
from hello import say as say_hello, name
from hi import say as say_hi

print(name)
say_hi()
say_hello()
