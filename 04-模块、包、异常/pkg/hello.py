name = "Hello PKG"

def say():
    print("hello PKG world")
    
class Nice:
    
    def __init__(self) -> None:
        self.name = "Hello PKG Nice"
        
    def __str__(self) -> str:
        return self.name