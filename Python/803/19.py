from math import *

x, y = input().split()

x = int(x)
y = int(y)

z1 = log(fabs((x + y) ** 2 + sqrt(fabs(y) + 2) - (x - (x * y) / (x ** 2 / 2 - 5))))
z2 = (cos(x + y) ** 2) / ((x + y) ** (1 / 3))
z = z1 + z2


print("%.2f" % z)