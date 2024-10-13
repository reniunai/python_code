"""
1. 声明Person类（class)

2. 根据Person类创建对象Object（可以创建多个）

3. 获取【属性】，调用对象的【方法】

函数、变量
"""

# 声明类
class Person:
    
    # 初始化函数/构造函数
    def __init__(self, name, age):
        """构造函数
        self （自己）不能少，代表当前创建的对象. 系统会自动传递这个参数进来
        :param name: 姓名
        :param age: 年龄
        """
        # print("__init__执行了!!!!!!!!!!!", name)
        self.name = name
        self.age  = age
        self.height = 175.0
        
    def eat(self):
        print("吃饭")
        
    def run(self):
        print(self.name + " 跑步")
        
    def say_hello(self, name):
        print("hello: ", name)
        
    def __str__(self) -> str:
        return "姓名：{}，年龄：{}".format(self.name, self.age)

# 创建对象1
p = Person("桑尼", 15)
print(p) # 姓名：xx，年龄：xx

# 创建对象2
p2 = Person("小红", 13)
print(p2)
