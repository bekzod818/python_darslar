n = int(input('Tangalar soni: '))

l = []
i = 1
while i <= n:
    t = int(input('Holati (gerb = 0, som = 1): '))
    l.append(t)
    i += 1

a = l.count(0)
b = l.count(1)

if a > b:
    print(b)
else:
    print(a)
