name = "Hello"

def say():
    print("hello world")
    
class Nice:
    
    def __init__(self) -> None:
        self.name = "Hello Nice"
        

# 需要作为主入口运行，或者想运行一些测试代码时，加一个判断即可

# 直接运行hello -> __name__ : "__main__"
print("__name__: " + __name__)

if __name__ == "__main__":
    say()
    print(Nice().name)

# 如果文件直接运行，           __name__ : "__main__"
# 如果作为其他文件一个模块导入，__name__ : "hello"