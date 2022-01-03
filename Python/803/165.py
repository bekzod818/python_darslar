from math import *

def f(a, b, c):
    x = (2 * a - b - sin(c)) / (5 + abs(c))
    return x


t, s = map(float, input().split())

natija = f(t, -2 * s, 1.17) + f(2.2, t, s - t)

print("%.2f" % natija)