x, y = map(float, input().split())

if x < 0 and y < 0:
    x = abs(x)
    y = abs(y)
elif x < 0 or y < 0:
    x = x + 0.5
    y = y + 0.5
print(x, y)