def index_error(index):
    """索引越界异常

    :param index: _description_
    """
    try:
        lst = [3,2,5]
        rst = lst[index]
    except IndexError as e:
        print(e)
        
    print("----------------------2")
    
def key_error(name):
    ages = {
        "张三" : 33,
        "李四" : 44
    }
    try:
        print(ages[name])
    except KeyError as e:
        print(f"{name}不存在")
    
def value_error():
    num_str = "123abc"
    try:
        num = int(num_str)
        print(num)
    except Exception as e:
        print(e)
        
    print("------------------")
    
class Person:
    
    def __init__(self) -> None:
        self.name = "zhangsan"
        
def attr_error():
    p = Person()
    print(p.name)
    print(p.say())
    print(p.age)
    
if __name__ == '__main__':
    # index_error(7)
    # key_error("李四2")
    value_error()
    # attr_error()