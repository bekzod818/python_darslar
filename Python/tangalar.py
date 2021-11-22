# l = [1, 5, 10, 25]

n = int(input())

cnt = 0

if n % 25 >= 0:
    butun = n // 25
    cnt += butun
    n %= 25

if n % 10 >= 0 and n < 25:
    butun = n // 10
    cnt += butun
    n %= 10

if n % 5 >= 0 and n < 10:
    butun = n // 5
    cnt += butun
    n %= 5

if n >= 1 and n < 5:
    cnt += n

print(cnt) 