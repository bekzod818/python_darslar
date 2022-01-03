from math import *

x, y, a, b = map(int, input().split())

s1 = 0
k = 1
i = 1
p1 = 1
while k <= a:
    while i <= b:
        p1 *= (i ** 2 + k ** (2 / i)) / ((sin(i) + cos(k)) * (i ** k))
        i += 1
    s1 += p1
    k += 1
    p1 = 1

print("%.2f" % s1)