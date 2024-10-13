class Animal:
    
    def __init__(self, name):
        self.name = name
        
    def eat(self):
        print(f"animal {self.name} is eating.")
        
    def sleep(self):
        print(f"animal {self.name} is sleeping.")
      
# interface
class 飞行能力:
    
    def 飞行(self):
        print(f"{self.name} is flying.")
        
class 游泳能力:
    
    def 游泳(self):
        print(f"{self.name} is swimming.")
    
    # def sleep(self):
    #     print(f"animal {self.name} is 边睡边游.")
        
class Duck(Animal, 飞行能力, 游泳能力):
    
    def __init__(self, name):
        super().__init__(name)

duck = Duck("唐老鸭")
duck.eat()
duck.sleep()
duck.飞行()
duck.游泳()