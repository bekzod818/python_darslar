from math import e

x, y = input().split()

x = float(x)
y = float(y)
t = x + y
a = abs((y ** 2 + 2) / (x + (x ** 3) / 5))
b = y ** 2
c = e ** (y + 2)

c1 = t / (b + a) + c 

print("%.2f" % c1)


