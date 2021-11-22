n = int(input())
arr = list(map(int, input().split()))[:n]

avg = sum(arr) / n
s = 0
cnt = 0
for i in arr:
    if  i < avg:
        s += i
        cnt += 1
res = s / cnt
print('%.2f' % (res))