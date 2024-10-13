# 定义变量
name = "张三丰"

# 定义函数
def mul(a, b):
    return a * b

# 定义类
class Person(object):
    
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        
    def __str__(self) -> str:
        return f"name: {self.name} age: {self.age}"
    
