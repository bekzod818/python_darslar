# from math import *
# n = int(input())
# cnt = 0
# i = 1
# while i < sqrt(n):
#     if n % i == 0:
#         cnt += 1
#     i += 1
# ildiz = sqrt(n)
# if fmod(n, ildiz) == 0:
#     print(2 * cnt + 1)
# else:
#     print(2 * cnt)
from math import *
n = int(input())
ildiz = sqrt(n)
if floor(ildiz) == ceil(ildiz):
    print(1)
else:
    print(0)

