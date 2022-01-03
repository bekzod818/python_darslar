a, b = input().split()

if a > b:
    print("Maksimal", a)
    print("Minimal", b)
elif a < b:
    print("Maksimal", b)
    print("Minimal", a)
else:
    print("Maksimal ham Minimal ham", b)
