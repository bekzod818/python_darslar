a, b, c = map(float, input().split())

# a = float(a)
# b = float(b)
# c = float(c)

if a > b and a > c:
    if b > c:
        print(a, c)
    elif b < c:
        print(a, b)
elif b > a and b > c:
    if a > c:
        print(b, c)
    else:
        print(b, a)
elif c > a and c > b:
    if a > b:
        print(c, b)
    else:
        print(c, a) 