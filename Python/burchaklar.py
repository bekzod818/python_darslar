from math import *

a, b, c = map(int, input().split())

alfa = acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
x = alfa * 180 / pi

beta = acos((c ** 2 + a ** 2 - b ** 2) / (2 * a * c))
y = beta * 180 / pi

fi = acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))
z = fi * 180 / pi
print("%.3f %.3f %.3f" % (x, y, z))