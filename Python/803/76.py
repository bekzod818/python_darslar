from math import *

a, b, c = map(int, input().split())

y = 0
h = 3

# for i in range(a, c + 1, 3):
#     y += ((a * i + b) / (b ** 2 + cos(i) ** 2)) ** (1 / 3) - sin(i ** 2) / (a * b)

x = a

while x <= c:
    y += ((a * x + b) / (b ** 2 + cos(x) ** 2)) ** (1 / 3) - sin(x ** 2) / (a * b)
    x += h

print("%.2f" % y)