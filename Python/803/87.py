from math import *

a = int(input())

y = 0
x = - pi / 2

while x <= pi:
    y += 2 * ((a ** sin(2 * x)) ** (1 / 3)) + x ** 2 * (cos(a * x))
    x += pi / 10

print("%.2f" % y)