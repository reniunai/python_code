import random
# 无参无返回
def hello():
    print("hello")
    

# 无参有返回
def get_rand():
    return random.randint(0, 10)

# 有参无返回
def say_hi(name):
    print("你好：", name)
    
# 有参有返回
def sum(a, b):
    return a + b

hello()
print(get_rand())
say_hi("小明")
print(sum(3, 5))