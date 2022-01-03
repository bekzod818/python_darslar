s = input()
t = ""
L, R = map(int, input().split())
if L < R:
    print(s[L-1:R])

else:
    for i in range(L, R - 1, -1):
        t += s[i-1]
    print(t)