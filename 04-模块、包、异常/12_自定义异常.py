class MyExcept(Exception):
    
    def __init__(self, msg):
        super().__init__()
        self.msg = msg
    
    def __str__(self) -> str:
        return self.msg
    
    
def name_input():
    """
    要求用户输入一个姓名
    1. 不能为空
    2. 长度不能超过4
    3. 不能包含数字
    
    raise异常时，此函数没有返回，raise后的代码不再执行
    """
    name = input("请输入姓名：")
    name = name.strip() # 去空格
    if name == "":
        raise MyExcept("姓名不能为空")
    elif len(name) > 4:
        raise MyExcept("姓名长度不能超过4")
    
    # a = 3 / 0
    for ele in name:
        if ele.isdigit():
            raise MyExcept("不能包含数字")
    return name

while True:
    try:
        name = name_input()
        print(name)
    except MyExcept as e:
        print("自定义异常：", e)
    except ZeroDivisionError:
        print("除零异常")
    except (IndexError, KeyError) as e:
        print("index或key异常", e)
    except Exception as e:
        print(e)
    