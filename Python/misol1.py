def raqam(num):
    cnt = 0
    while num > 0:
        cnt += num % 10
        num = num // 10
    s = cnt ** 2

    return s

for i in range(1, 100):
    s = raqam(i)
    if i % s == 0:
        print(i)
    