n = int(input())
arr = list(map(int, input().split()))[:n]

k = int(input())

x = arr[k - 1]
mx = max(arr)

for i in range(n):
    if mx == arr[i]:
        arr[i] = x

arr[k-1] = mx

for i in arr:
    print(i, end=" ")

