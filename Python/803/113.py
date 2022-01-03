n = int(input())
arr = list(map(int, input().split()))[:n]

manfiy = []

for i in arr:
    if i < 0:
        manfiy.append(i)
s = sum(manfiy) / len(manfiy)
print("%.2f" % s)
