s = input()
t = ""
for i in s:
    if i.islower():
        t += i.upper()
    elif i.isupper():
        t += i.lower()
    else:
        t += " "
print(t)