from math import *

a, b, c, d = map(int, input().split())

s = 0
p = 1

for m in range(1, a + 1):
    s += (3 * (m ** 3) + 4 * m + 5) / (m ** 3 + log(m))


for k in range(1, b + 1):
    p *= (k) / (k ** 3 + 7 * k + 5)

s1 = 0
p1 = 1
for i in range(1, c + 1):
    for m in range(1, d + 1):
        p1 *= (log(i) + m ** i) / (m ** i) 
    s1 += p1


print('%.2f %.2f %.2f' % (s, p, s1))