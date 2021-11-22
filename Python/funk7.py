def bolinish(n):
    for i in range(2, 11):
        if n % i == 0:
            print(f"{n} soni {i} ga bo'linadi")
x = int(input())
bolinish(x)