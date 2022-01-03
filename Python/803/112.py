n = int(input())
arr = list(map(int, input().split()))[:n]

s = 0
p = 1

for i in range(n):
    if i % 2 == 0:
        p *= arr[i]
    else:
        s += arr[i]

x = p / s
print("%.2f" % x)