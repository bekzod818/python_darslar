n = int(input())
s = list(input().split())[:n]

t = ""
l = []
for i in s:
    for j in i:
        if j != "$":
            t += j
    l.append(t)
    t = ""

for i in l:
    print(i, end=" ")
