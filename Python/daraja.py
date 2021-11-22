from math import *
A, B = map(int, input().split())
d = int(fmod(A, 10))

if d == 2 or d == 3 or d == 8 or d == 7:

    if B%4==1:
        print(d)
    if B%4==2:
        print(int(fmod((d ** 2), 10)))
    if B%4==3:
        print(int(fmod((d ** 3), 10)))
    if B%4==0:
        print(int(fmod((d ** 4), 10)))
if d==4 or d==9:
    if B%2==1:
        print(d)
    if B%2==0:
        print(int(fmod((d ** 2), 10)))
if d==5:
    print(5)
if d==6:
    print(6)
if d==0:
    print(0)
if d==1:
    print(1)