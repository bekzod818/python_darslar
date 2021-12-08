from math import sin, factorial
n = int(input())

s = 0
# for i in range(1, n + 1):
#     s += sin(i) / (2 ** i)

i = 1
while i < n + 1:
    s += sin(i) / (2 ** i)
    i += 1

print('%.2f' % s)