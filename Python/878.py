n = int(input())

s = 0
s1 = ""

for i in range(1, n + 1):
    s1 += str(i)
    s += int(s1)

print(s % 10007)