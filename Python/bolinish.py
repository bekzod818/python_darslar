n = int(input())

if n % 2 == 0 and n % 3 == 0:
    print('double')
elif n % 2 == 0:
    print(2)
elif n % 3 == 0:
    print(3)
else:
    print('none')