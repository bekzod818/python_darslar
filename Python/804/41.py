x, y, z = map(float, input().split())

if x < 1 and y < 1 and z < 1:
    m = min(x, y, z)
    if x == m:
        x = (y + z) / 2
    elif y == m:
        y = (x + z) / 2
    elif z == m:
        z = (x + y) / 2

print(x, y, z)
