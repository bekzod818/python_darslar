a = int(input())
b = int(input())

m = max(a, b)

if m == a:
    if a % b == 0:
        print(True)
    else:
        print(False)
else:
    if b % a == 0:
        print(True)
    else:
        print(False)