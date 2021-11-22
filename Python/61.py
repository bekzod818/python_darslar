from math import sin, factorial
n = int(input())

s = 0
for i in range(1, n + 1):
    s += sin(i) / (2 ** i)
print('%.2f' % s)