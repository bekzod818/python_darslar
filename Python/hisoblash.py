from math import *
a, b, c, x, y = input().split()

a = int(a)
b = int(b)
c = int(c)
x = float(x)
y = float(y)

z1 = x ** (1/6) + sqrt(a ** 2 + b ** 2)
z2 = (log(y) / log(x)) / (c ** 3)
z3 = abs(sin(x) + cos(y))
Z = z1 + z2 - z3 + 2 / 5

print('%.3f' % Z)


