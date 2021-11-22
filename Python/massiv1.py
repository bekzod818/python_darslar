from math import log

n = int(input())
arr = list(map(int, input().split()))[:n]

l = log(sum(arr) / n)

for i in range(n):
    if arr[i] < 0:
        arr[i] = l

print(arr)