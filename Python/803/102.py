n = int(input())
arr = list(map(int, input().split()))[:n]

a, b = map(int, input().split())
mn = min(arr)
for i in range(n):
    if a <= i + 1 <= b:
        arr[i] = arr[i] / mn
    print("%.1f" % arr[i], end = " ")