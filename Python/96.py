from math import *

x,y,c,d = map(int, input().split())

s, p, s1, p1 = 0, 1, 0, 1

for k in range(1, x + 1):
    s += (((-1) ** k) * (k + 1)) / (k ** 3 + k ** 2 + 1)

for i in range(1, y + 1):
    p *= (i ** 3 + abs(i - 9)) / (log(i) + 7 * i)

for n in range(1, c + 1):
    s1 = 0
    for m in range(1, d + 1):
        s1 += (log(m + 5)) / (m ** (n + 3) + n * m) * ((-1) ** m)
    p1 *= s1

print("%.2f %.2f %.2f" % (s, p, s1))