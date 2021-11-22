n = int(input())

l = [-1]
i = 0
for j in range(3, 2 * n, 2):
    l.append(l[i] + j)
    i += 1

print(l[n-1])