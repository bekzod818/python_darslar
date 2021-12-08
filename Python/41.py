x, y, z = map(float, input().split())

m = min(x, y, z)
if x < 1 and y < 1 and z < 1:
    if m == x:
        x = (y + z) / 2
    elif m == y:
        y = (z + x) / 2
    else:
        z = (x + y) / 2

print(x, y, z)

# else:
#     print(x, y, z)
