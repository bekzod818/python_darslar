a, b, c = map(float, input().split())
# a = int(a)
# b = int(b)
# c = int(c)

if a > b and a > c:
    if b > c:
        print("Max", a)
        print("Min", c)
    else:
        print("Max", a)
        print("Min", b)
elif b > a and b > c:
    if a > c:
        print("Max", b)
        print("Min", c)
    else:
        print("Max", b)
        print("Min", a)
elif c > a and c > b:
    if a > b:
        print("Max", c)
        print("Min", b)
    else:
        print("Max", c)
        print("Min", a)

elif a == b:
    pass




# n = int(input())

# if n == 1:
#     print("Dushanba")
# elif n == 2:
#     print("Seshanba")
# elif n == 3:
#     print("Chorshanba")
# else:
#     print("1 dan 3 gacha son kiriting")




# a = float(input())
# b = float(input())

# if a > b:
#     print("a soni b dan katta")
# elif a < b:
#     print("b soni a sonidan katta")
# else:
#     print("a soni b soniga teng")

    