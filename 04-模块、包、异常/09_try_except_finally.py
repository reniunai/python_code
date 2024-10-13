def read_file():
    
    a = 10
    b = 5
    
    try:
        rst = a / b
        print(rst)
        
        print("计算之后，正常运行代码")
        return rst
    except ZeroDivisionError as e:
        print("除数不能为0")
    finally:
        print("finllay关闭资源，无论是否有异常，都会执行")
        
"""
try-except
try-finally
try-except-finally
"""
def write_file():
    # 打开文件
    f = open("haha.txt", "w")
    
    try:
        a = 10
        b = 23
        rst = a / b
        
        f.write(f"rst: {rst}")
    # except Exception as e:
    #     print("出现异常", e, type(e))
    finally:
        f.close()
        print("关闭资源")
        
if __name__ == '__main__':
    # read_file()
    write_file()
