from math import *

def f(a, b, c):
    d = (2 * a - b - sin(c)) / (5 + abs(c))
    return d

t, s = map(float, input().split())

s = f(t, -2 * s, 1.17) + f(2.2, t, s - t)

print('%.2f' % s)

