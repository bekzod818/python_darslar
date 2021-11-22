def computeGcd(a, b):
    if b == 0:
        return a
    else:
        return computeGcd(b, a%b)

def gcd(a, b):
    if a < b:
        return gcd(a, b - a)
    elif a > b:
        return gcd(a - b, b)
    else:
        return a


# n = int(input())

# for i in range(1, n + 1):
#     print(i * "#")
    # print((n - i) * " " + 2 * i * "*")



n = int(input())
for i in range(1,n+1):
    print('  '*(n-i), end='')
    for j in range(1,i + 1):
        print(j, end=' ')
    print()

# n = int(input())
# for i in range(1,n+1):
#     print('  '*(n-i), end='')
#     for j in range(i, 0, -1):
#         print(j, end=' ')
#     print()

# from math import gcd

# a, b = map(int, input().split())
# print(gcd(a, b))


# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end = ' ')
#     print()