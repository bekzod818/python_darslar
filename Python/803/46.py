a = float(input())

if a >= 2:
    y = 4
elif -1 <= a < 2:
    y = a ** 2
elif a < -1:
    y = 1 / (a ** 2)

print("%.2f" % y)