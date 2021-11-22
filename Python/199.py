s = input()

unli = ['a', 'i', 'u', 'o', 'e']
label = True
for i in range(len(s) - 2):
    if s[i] not in unli and s[i + 1] not in unli and s[i + 2] not in unli:
        label &= False
if label:
    print("YES")
else:
    print("NO")