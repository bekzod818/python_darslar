#1 va 2
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car != "gm":
        print(car.title())
    else:
        print(car.upper())
#3
login = input("Login kiriting: ")
if login == 'admin':
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {login}")