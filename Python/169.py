def Min(a, b):
    if a < b:
        return a
    else:
        return b

def Max(x, y):
    if x > y:
        return x
    else:
        return y

a, b = map(float, input().split())

u = Min(a, b)
v = Min(a * b, Max(a, b))
s = Min(u + v, 3.14)

print('%.2f %.2f %.2f' % (u, v, s))