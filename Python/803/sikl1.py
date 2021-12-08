from math import *

n = int(input())

s = 0

for i in range(1, n + 1):
    s += ((-1) ** (i - 1)) * (sin(i ** i)) / (2 ** i)

print("%.2f" % s)