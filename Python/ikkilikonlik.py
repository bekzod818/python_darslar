a = int(input())
b = int(input())
# l = []
if a == 10:
    l = bin(b)
    print(l[2:])
    # while True:
    #     if b // 2 < 2:
    #         l.append(b % 2)
    #         break
    #     else:
    #         l.append(b % 2)
    #         b //= 2
    # l.append(1)
    # s = ""
    # for i in l[::-1]:
    #     s += str(i)
    # print(int(s))
elif a == 2:
    print(int(str(b), 2))
    # res = 0
    # b = str(b)
    # b = b[::-1]
    # for i in range(len(b)):
    #     res += int(b[i]) * (2 ** i)
    # print(res)
