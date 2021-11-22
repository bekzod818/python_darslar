s = input()

l = len(s) // 2

if s[:l] == s[l:]:
    print("YES")
else:
    print("NO")