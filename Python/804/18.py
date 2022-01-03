from math import *

x, y = input().split()

x = float(x)
y = float(y)

a = 1 / (x + 2 / (x ** 2) + 3 / (x ** 3)) + e ** (x ** 2 + 3 * x)
b = atan(x + y) + abs(5 + x) ** 2
c = cos(y ** 2 + (x ** 2) / 2) ** 2

f2 = a / b - c

print("%.2f" % f2)