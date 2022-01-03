v = float(input("Tezlikni kiriting: "))


if v <= 75:
    print("Qoida buzmadingiz")
elif 75 < v <= 90:
    print("1 EKIH jarima")
elif 90 < v <= 110:
    print("5 EKIH jarima")
elif 110 < v <= 130:
    print("10 EKIM jarima")
else:
    print("20 EKIH jarima")