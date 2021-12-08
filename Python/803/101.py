n = int(input())
arr = list(map(int, input().split()))[:n]

average = sum(arr) / n

kichik = []

for i in range(n):
    if arr[i] < average:
        kichik.append(arr[i])

x = sum(kichik) / len(kichik)
print("%.2f" % x)

