s = input().split()
l = []
for i in s:
    x = len(i)
    l.append(x)
mx = max(l)

for i in s:
    if len(i) == mx:
        print(i)