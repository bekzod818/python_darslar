n = int(input())
arr = list(map(int, input().split()))[:n]
x, y = map(int, input().split())
cnt = 0
for i in arr:
    if x >= i or i > y:
        cnt += 1  

print(cnt)