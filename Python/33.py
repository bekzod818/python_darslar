x, y, z = map(int, input().split())

mx = max(x + y + z, x, y, z)
mn = min(x + y / 2, x, y, z)

print("%.2f %.2f" % (mx, mn ** 2))