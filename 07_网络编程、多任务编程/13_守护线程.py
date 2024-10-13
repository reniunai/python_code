import time
import threading

def eat():
    print("吃饭")

def singing():
    print("singing线程：", threading.currentThread())
    for i in range(10):
        print("唱歌...", i)
        time.sleep(0.5)
        
def dancing():
    print("dancing线程：", threading.currentThread())
    for i in range(10):
        print("跳舞...", i)
        time.sleep(0.5)
    
    
if __name__ == '__main__':
    print("主线程：", threading.currentThread())
    t1 = threading.Thread(target=singing)
    t1.daemon = True    # 将子线程设置为守护线程
    t1.start()

    t2 = threading.Thread(target=dancing)
    t2.daemon = True    # 将子线程设置为守护线程
    t2.start() 
    
    # 不要在start之后设置，否则# RuntimeError: cannot set daemon status of active thread
    # t2.daemon = True    # 将子线程设置为守护线程 
    
    # 必须所有子线程都设置daemon=True，才能完全退出
    # 只要有一个线程没有设置，所有其他线程正常运行
    time.sleep(2)
    print("主线程执行完毕，退出程序")
    exit(0)
    print("-------------abc")
