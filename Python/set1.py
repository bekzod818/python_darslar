set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
set3 = set1.intersection(set2)

if len(set3) > 0:
    print(set3)
else:
    print("no")  