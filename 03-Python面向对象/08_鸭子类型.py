class Dog:
    
    def eat(self):
        print("狗吃骨头")

    def run(self):
        print("狗跑起来了")

# 函数
def someone_eat(duck):
    """
    要求传进来一个拥有eat和run的对象
    """
    # 准备吃饭餐座
    
    duck.eat()
    
    duck.run()
    
    # 清理餐座
    
dog = Dog()
someone_eat(dog)