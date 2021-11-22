from math import factorial as f

n = int(input())

fact = str(f(n))
fact = fact[::-1]
for i in fact:
    if i == "0":
        continue
    else:
        print(i)
        break