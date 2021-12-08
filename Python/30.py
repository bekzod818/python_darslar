from math import *
x, y, z = input().split()

x = int(x)
y = float(y)
z = float(z)

AF = (2 ** (-x)) * sqrt(x + (abs(y) + 2) ** (1 / 4)) * ((exp(x - 1) / (sin(z + 2)) + 2) ** (1 / 3))

print("%.2f" % AF)