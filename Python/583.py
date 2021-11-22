n = int(input())
arr = list(map(int, input().split()))[:n]
p = 1
for i in arr:
    p *= i

ikkilik = bin(p)
ikkilik = ikkilik[::-1]

if ikkilik.find("1") != -1:
    print(ikkilik.find("1"))
else:
    print(0)