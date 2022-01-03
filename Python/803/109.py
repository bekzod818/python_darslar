from math import log

n = int(input())
arr = list(map(int, input().split()))[:n]

M = int(input())
p = 1
for i in arr:
    if i > M:
        p *= i

print("%.2f" % log(p))