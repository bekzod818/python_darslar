x, y = map(int, input().split())

if x > y:
    x1 = 4 * x * y
    y1 = (x + y) / 2
    # print("%.1f %.1f" % (4 * x * y, (x + y) / 2))

else:
    y1 = 4 * x * y
    x1 = (x + y) / 2
    # print("%.1f %.1f" % ((x + y) / 2, 4 * x * y))

print("%.1f %.1f" % (x1, y1))