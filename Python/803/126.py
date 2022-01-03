from math import *

n = int(input())
arr = list(map(int, input().split()))[:n]

l = log(sum(arr) / len(arr))

for i in range(n):
    if arr[i] < 0:
        arr[i] = l

for i in arr:
    print("%.2f" % i, end=" ")