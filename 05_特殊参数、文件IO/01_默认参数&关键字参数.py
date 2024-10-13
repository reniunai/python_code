print("------------------------------------默认参数")
def say_hello(score, name="刘亦菲"):    # positional argument: 'name'
    print(f"你好：{name} 得分：{score}")
    
# 拥有默认值的参数，要放到参数最后
say_hello(90)
say_hello(88, "迪丽热巴")

print("-----------------------------------关键字参数")

def show_info(name, age=18, height=170.0):
    print(f"姓名：{name} 年龄：{age} 身高：{height}")
    
show_info("流川枫")
show_info("流川枫", 22)
show_info("流川枫", age=36)
show_info("流川枫", height=180.0)
# show_info(height=180.0, "流川枫")   # positional argument follows keyword argument
show_info(height=185.0, name="流川枫", age=23)   # positional argument follows keyword argument
