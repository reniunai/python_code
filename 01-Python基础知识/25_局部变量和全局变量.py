g = None

def func_a():
    a = 10
    
    # 声明后边用到的变量g是全局的, 如果g不存在，则自动创建
    global g
    g = 456
    print("a =", a)
    print("a_g =", g)
    
def func_b():
    print("b_g =", g)
    
func_a()
func_b()