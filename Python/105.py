n = int(input())
arr = list(map(int, input().split()))[:n]

a, b = map(int, input().split())
s = 0
cnt = 0

for i in range(n):
    if not a <= i + 1 <= b:
        s += arr[i]
        cnt += 1
res = s / cnt
print('%.2f' % res)