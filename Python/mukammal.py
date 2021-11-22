def isPerfect(n):
    sum = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum = sum + i + n/i
        i += 1 
    return (True if sum == n and n!=1 else False)

n = int(input())
cnt = 0
l = []
for i in range(1, n + 1):
    if isPerfect(i):
        l.append(i)
        cnt += 1

print(cnt)
for i in l:
    print(i, end=" ")


# l = []
# s=0
# cnt=0
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,i):
#         if i%j==0:
#             s+=j
#     if s==i:     
#         l.append(i)
#         cnt+=1
#     s=0
# print(cnt)

# for i in l:
#     print(i, end=" ")


