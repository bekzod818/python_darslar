from math import sin, fabs, sqrt, tan

x1, x2, c, d = input().split()

x1 = float(x1)
x2 = float(x2)

c = int(c)
d = int(d)

surat = sin(abs(c * (x2 ** 3) + d * (x1 ** 3) - c * d)) ** 2
maxraj = sqrt(c * (x1 ** 2) + d * (x2 ** 2) + 7)
t = tan(x1 * (x2 ** 2) + d ** 3)

F = abs(surat / maxraj) + t


# F = fabs((sin(abs(c * (x2 ** 3) + d * (x1 ** 3) - c * d)) ** 2) / (sqrt(c * (x1 ** 2) + d * (x2 ** 2) + 7))) + tan(x1 * (x2 ** 2) + d ** 3)

print("%.2f" % F)