class WashMachine:

    def __init__(self, brand, capacity):
        """洗衣机的初始化函数

        :param brand: 品牌
        :param capacity: 容量
        """
        self.brand = brand
        self.capacity = capacity
        # 门状态
        self.is_closed = False
        # 模式：0:未设定模式，1：轻揉模式，2：狂揉模式
        self.__mode = 0
        # 转速
        self.__motor_speed = 0

    def open_door(self):
        self.is_closed = False
        print("打开洗衣机门")

    def close_door(self):
        self.is_closed = True
        print("关闭洗衣机门")
        
    def set_mode(self, new_mode):
        """设置洗衣模式
        0: 未设定模式，
        1: 轻揉模式，
        2: 狂揉模式
        :param new_mode: 模式
        """
        if new_mode not in [1, 2]:
            print("模式设置错误")
            return
        
        self.__mode = new_mode
        
    def __set_motor_speed(self, speed):
        self.__motor_speed = speed
        
    def wash(self):
        # 检查洗衣机门是否关闭
        if not self.is_closed:
            print("请关闭洗衣机门，哔哔哔..")
            return
        
        # 检查洗衣模式是否设置
        if self.__mode == 0:
            print("请设置洗衣模式")
            return
        
        print("放水...")
        print("放满了...")
        if self.__mode == 1:
            print("轻柔模式，洗内衣")
            # 调节马达转速
            self.__set_motor_speed(1000)
            print("马达转速: ", self.__motor_speed)
        elif self.__mode == 2:
            print("狂揉模式，洗大衣")
            # 调节马达转速
            self.__set_motor_speed(2000)
            print("马达转速: ", self.__motor_speed)
        
        print("开始洗衣服")
        print("洗衣结束")


# 创建对象
machine = WashMachine("海尔", 10)
machine.open_door()
machine.close_door()
machine.set_mode(2)
# 细节封装到对象的方法内部
machine.wash()