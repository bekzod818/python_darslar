n = int(input())
s = list(input().split())[:n]

a = s.count("A")
b = s.count("S")
d = s.count("L")
e = s.count("O")
f = s.count("M")

if a >= 2 and b >= 2 and d >=1 and e >= 1 and f >= 1:
    print("YES")
else:
    print("NO")