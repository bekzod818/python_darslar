n = int(input())
label = ''
if n == 2:
    label = "tub"
else:
    for i in range(2, n):
        if n % i == 0:
            label = "tub emas"
            break
        else:
            label = "tub"

print(label)