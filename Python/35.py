a, b, c = map(int, input().split())

if c <= b <= a:
    a *= 2
    b *= 2
    c *= 2
else:
    a, b, c = abs(a), abs(b), abs(c)

print(a, b, c)