from math import *

x,y,a,b = map(int, input().split())

s, p, s1 = 0, 1, 0

a = 1
while a <= x:
    s += (a ** 2 + 2 * a) / (a ** 3 + a * cos(a) ** 2 + 1)
    a += 1


for i in range(1, y + 1):
    p *= (i ** 2 + 1) / (i ** (3 / i) + 2)

# for i in range(1, a + 1):
#     p1 = 1
#     for k in range(1, b + 1):
#         p1 *= log(k ** i + k ** (1 / i)) - log(k ** 3 + i ** (1 / k))
#     s1 += p1
i = 1

while i <= a:
    k = 1
    p1 = 1
    while k <= b:
        p1 *= log((k ** i + k ** (1 / i)) / (k ** 3 + k ** (1 / k)))
        k += 1
    s1 += p1
    i += 1

print("%.2f %.2f %.2f" % (s, p, s1))

# from math import *

# x, y, a, b = map(int, input().split())

# s = 0
# p = 1
# s1 = 0
# p1 = 1

# for a in range(1, x + 1):
#     s += ((a ** 2) + 2 * a) / ((a ** 3) + a * (cos(a) ** 2) + 1)

# for i in range(1, y + 1):
#     p *= ((i ** 2) + 1) / (((i ** 3) ** (1 / i)) + 2)

# for i in range(1, a + 1):
#     p1 = 1
#     for k in range(1, b + 1):
#         p1 *= log(((k ** i) + k ** (1 / i)) / ((k ** 3) + i ** (1 / k)))
#     s1 += p1
# print("%.2f %.2f %.2f" % (s, p, s1))