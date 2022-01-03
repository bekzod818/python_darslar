a, b, c = map(int, input().split())

if a >= b >= c:
    print(2 * a, 2 * b, 2 * c)
else:
    print(abs(a), abs(b), abs(c))