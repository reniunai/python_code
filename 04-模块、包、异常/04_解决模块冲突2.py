# 2. 导入全部内容冲突
# from hello import *
# from hi import *
import hello
import hi

print(hello.name)
hi.say()
hello.say()

print(hi.Nice().name)
print(hello.Nice().name)