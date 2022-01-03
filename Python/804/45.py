from math import *

a, b, c = map(int, input().split())

D = b ** 2 - 4 * a * c

if D > 0:
    x1 = (-b - sqrt(D)) / (2 * a)
    x2 = (-b + sqrt(D)) / (2 * a)
    print("%.2f %.2f" % (x1, x2))
elif D == 0:
    x = (-b) / (2 * a)
    print("%.2f %.2f" % (x, x))
else:
    print("NO")