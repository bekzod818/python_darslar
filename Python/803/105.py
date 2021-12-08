n = int(input())
arr = list(map(int, input().split()))[:n]

a, b = map(int, input().split())
l = []
for i in range(n):
    if not a <= i + 1 <= b:
        l.append(arr[i])

x = sum(l) / len(l)
print("%.2f" % x)