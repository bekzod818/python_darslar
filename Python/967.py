n = int(input())
arr = list(map(int, input().split()))[:n]
s1 = s2 = 0
for i in range(n):
    for j in range(n):
        s2 += arr[i] // arr[j]
    s1 += s2

print(s2)