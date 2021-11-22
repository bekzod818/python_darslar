n = int(input())
arr = list(map(int, input().split()))[:n]

s = 0
for i in arr:
    if i % 2 == 1:
        s += 1

print(s ** 2)