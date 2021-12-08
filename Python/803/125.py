n = int(input())

l = False
for i in range(3, n + 1, 2):
    if n % i == 0:
        l = l | True
    
if l:
    print("Yes")
else:
    print("No")
    