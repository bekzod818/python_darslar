m, n = map(int, input().split())

def raqamlar_sum(n):
    s = 0
    for i in str(n):
        s += int(i)
    return s

t = tuple(range(1, 10 ** 7))
l = []
for i in t:
    if m == raqamlar_sum(i):
        l.append(i)
    if len(l) >= n:
        break

print(l[n-1])