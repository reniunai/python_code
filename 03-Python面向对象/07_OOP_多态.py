# 父类
class Human:
    
    def eat(self):
        print("人类吃饭")
        
# 中国人
class ZhHuman(Human):
    
    def eat(self):
        print("中国人用筷子吃饭")
        
# 美国人
class UsHuman(Human):
    
    def eat(self):
        print("美国人用刀叉吃饭")
        
# 印度人
class IndiaHuman(Human):
    
    def eat(self):
        print("印度人手抓饭吃饭")
        
# 函数
def someone_eat(someone: Human, score: int):
    """接受一个具备eat方法的对象"""
    someone.eat()
    
    # print(score, type(score))

# 创建对象        
human = Human()
zh_man = ZhHuman()
us_man = UsHuman()
in_man = IndiaHuman()

someone_eat(human, 0)
someone_eat(zh_man, 1.3)
someone_eat(us_man, "22")
someone_eat(in_man, True)

