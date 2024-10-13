string = "Hello World 你好世界"

for s in string:
    print(s, end=" ")
    
print()
print("H" in string)
print("h" in string)
print("你好" in string)
print("好你" in string)
print("嘎嘎" not in string)