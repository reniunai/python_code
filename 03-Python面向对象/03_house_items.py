# --------------------------------- Item 家具类
class Item:
    
    def __init__(self, name, area):
        """家具类的初始化方法

        :param name: 家具的名称
        :param area: 家具占地面积
        """
        self.name = name
        self.area = area

    def __str__(self) -> str:
        return "str家具名称：{}, 占地面积：{}".format(self.name, self.area)
    
    def __repr__(self) -> str:
        return "repr家具名称：{}, 占地面积：{}".format(self.name, self.area)

# ---------------------------------- House 房子类
class House:
    
    def __init__(self, addr, area) -> None:
        """房子的初始化方法

        :param address: 房子地址
        :param area: 套内面积
        """
        self.address = addr
        self.area = area
        # 剩余面积
        self.free_area = self.area
        # 家具列表
        self.items = []
        
    def add_item(self, item):
        """添加家具到房子中
        
        剩余面积>=家具占地面积
        :param item: 要添加的家具
        """
        if self.free_area >= item.area:
            # 添加到家居列表
            self.items.append(item)
            # 修改剩余面积
            self.free_area -= item.area
            print("添加成功", item.name)
        else:
            print("面积不足，无法添加", item.name)

    def __str__(self) -> str:
        return "房子地址：{} 套内面积：{} 剩余面积：{}".format(self.address, self.area, self.free_area)

# 主程序逻辑
# 1. 创建 家具对象, 输出 家具信息
item1 = Item("沙发", 10)
item2 = Item("餐桌套装", 40)
item3 = Item("家庭影院", 45)
print(item1)
print(item2)
print(item3)

# 2. 创建 房子对象, 输出 房子信息
house = House("光谷御府1期", 100)
print(house)

# 3. 房子添加家具, 输出 房子信息
house.add_item(item1)
house.add_item(item2)
house.add_item(item3)
print(house, "家具个数：" ,len(house.items))
print(house.items)
