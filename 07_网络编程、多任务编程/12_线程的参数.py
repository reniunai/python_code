import threading
import time

def singing(name, age=18, score=100):
    for i in range(5):
        print(f"{name}({age})唱歌，得分:{score}, {i}")
        time.sleep(0.5)
        
if __name__ == '__main__':
    # 传递参数方式1：元组args， 只有一个元素，要记得加逗号(10,)
    # thread = threading.Thread(target=singing, args=("张靓颖",))
    # 传递参数方式2：字典kwargs，不要求顺序，没有默认值的参数，必须传参
    # thread = threading.Thread(target=singing, kwargs={"age":30, "name":"李宇春"})
    
    # 传递参数方式3：元组+字典 （元组里的内容不可以和字典里的内容冲突）
    thread = threading.Thread(target=singing, args=("张靓颖",), kwargs={"age":30, "score": 88})
    thread.start()
    
    # 线程创建和启动不会阻塞当前线程
    print("---------------")
