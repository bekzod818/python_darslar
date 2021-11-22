from math import log
n = int(input())
arr = list(map(int, input().split()))[:n]

m = int(input())
p = 1
for i in range(n):
    if arr[i] > m:
        p *= arr[i]

print('%.2f' % log(p))
