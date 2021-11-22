a, b, c = map(int, input().split())

y = 0
i = a
while i <= b:
    y = y + (a ** b + b ** i + c ** a) / (2 * (i ** 2) + 3 * (a ** i))
    i += 2

print('%.2f' % y)
