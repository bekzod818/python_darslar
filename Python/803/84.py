from math import *

a, b, c = map(int, input().split())

s = 0
x = -1

while x <= 1:
    s += ((sin(a * x) + b ** c) / (b ** 2 + cos(x) ** 2)) ** (1 / 3) - (sin(x ** 2)) / (a * b)
    x += 0.25

print("%.2f" % s)