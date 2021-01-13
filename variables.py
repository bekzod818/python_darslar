ism = 'Bekzod' 
def salom():
    global ism #Global o'zgaruvchi
    ism = 'Azim'
    print(f"Assalomu aleykum {ism}")
x, y, z = 'Orange', 'Banana', 'Cherry'
fruits = ["apple", "banana", "cherry"]
a, b, c = fruits
print(f"{a.title()} {b.title()} {c.title()}")
salom()
print(f"Assalomu aleykum {ism}")