
for row in range(1, 6):
    for column in range(1, row + 1):
        print(column, end=' ')
    print()
print("-" * 20)
for row in range(6, 0, -1):
    for column in range(row - 1, 0, -1):
        print(column, end=" ")
    print()

num = int(input("Number = "))
count = 0
while num != 0:
    num //= 10
    count += 1
print(count)

n = -10
while n <= -1:
    print(n)
    n += 1
