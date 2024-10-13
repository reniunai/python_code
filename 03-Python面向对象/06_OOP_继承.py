# ------------------------------------------ 定义Person类

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def say_hello(self):
        print("say hello from: ", self.name)
        
        
# ------------------------------------------- 定义学生类Student继承Person

class Student(Person):
    
    def __init__(self, name, age, score):
        # 调用父类的初始化方法
        super().__init__(name, age)
        # 定义自己的属性
        self.score = score

    def play(self):
        print(self.name, "打游戏")
    

# 创建学生
stu = Student("小明", 17, 99.5)
# 访问父类方法
stu.say_hello()
# 访问自己的方法
stu.play()
# 访问属性
print("name: {} age:{} score:{}".format(stu.name, stu.age, stu.score))
