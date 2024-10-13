def hello():
    try:
        arr = [1,2,3]
        # a = arr[10]
        
        print("-----0")
        return 0
    except Exception:
        print("-----1")
        return 1
    finally:
        print("-----2")
        # 如果finally里有return，则必走finally
        return 2
    
def hello2():
    try:
        arr = [1,2,3]
        a = arr[10]
        
        print("-----0")
        return 0
    except Exception:
        print("-----1")
    finally:
        print("-----2")
        # 如果finally里有return，则必走finally

    return -1
    
# print(hello())
print(hello2())
