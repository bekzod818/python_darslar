from math import *

x1, x2, c, d = input().split()

x1 = float(x1)
x2 = float(x2)
c = int(c)
d = int(d)

a = sin(abs(c * x2 ** 3 + d * x1 ** 3 - c*d)) ** 2
b = sqrt(c * x1 ** 2 + d * x2 ** 2 + 7)

F = abs(a / b) + tan(x1 * x2 ** 2 + d ** 3)

print("%.2f" % F)