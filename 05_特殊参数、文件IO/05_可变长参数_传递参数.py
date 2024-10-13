scores = [34, 46, 64, 72, 23, 54]

def average(*args):
    return sum(args) / len(args)

# *scores对这个列表或元组进行解包
print(average(2,4,6))
print(average(*[2,4,6]))
print(average(*scores))

def show_info(**kwargs):
    print("kwargs: ", kwargs)
    
stu = {
    "name": "lisi",
    "height": 170.0
}
    
show_info(name="zhangsa", age=13)
# **stu对这个字典进行解包
show_info(**stu)