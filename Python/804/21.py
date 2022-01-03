a, b = input().split()

a = float(a)
b = float(b)

T = a ** (1 / 5) + (b * (a + b) / (2 * b + a * b)) ** (1 / 4) * (a ** 2 + b ** 2 + 2)

print("%.2f" % T)

