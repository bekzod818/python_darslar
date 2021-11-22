def kopaytma(*sonlar):
    p = 1
    for i in sonlar:
        p *= i
    return p

def summa(x, y, *sonlar):
    return sum(sonlar) + x + y

print(kopaytma(1, 2, 3, 5))
print(summa(3, 4, -4, 3, 5, 8, -3))