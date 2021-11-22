s = input().split(":")
l = []
for i in s:
    l.append(int(i))

for i in sorted(l):
    print(i, end=" ")