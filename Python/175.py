s = input().split("(")
res = ""
for i in s:
    ind = i.find(")")
    if ind == -1:
        res += i
    elif ind != -1:
        j = i[ind+1::]
        i = i[ind-1::-1] + j
        res += i

print(res)
