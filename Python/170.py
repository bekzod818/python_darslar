def h(a, b):
    c = a / (b ** 2 + 1) + b / (a ** 2 + 1) - (a - b) ** 3
    return c

def Max(x, y):
    if x > y:
        return x
    else:
        return y

s, t = map(float, input().split())

d = h(s, t) + Max(h(s - t, s * t), h(s - t, s + t)) + h(1, 1)

print('%.2f' % d)
