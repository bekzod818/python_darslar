# if (agar)
cars = ['audi', 'toyota', 'subaru', 'bmw']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
# teng emaslik sharti
while True:
    answer = int(input("4 * 8 = "))
    if answer != 32:
        print("Xato! Yana urinib ko'ring.")
    else:
        print("To'g'ri javob qoyil.")
        break 

# in va not in
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
print(user in banned_users)
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
else:
    print(f"Banned")

# if elif else
age = int(input("Yoshingiz nechada? "))
if age <= 8:
    narh = 0
elif age <= 18:
    narh = 5000
elif 18 < age < 60:
    narh = 12000
else:
    narh = 0
if narh != 0:
    print(f"Kirish {narh} so'm.")
else:
    print("Kirish bepul.")

# ifni list bilan ishlatish
cars = ['audi', 'bmw', 'toyota', 'ferrari', 'lamborgini', 'mercedes', 'malibu']
salon = ['audi', 'toyota', 'ferrari', 'mercedes']
for car in cars:
    if car not in salon:
        if car != 'bmw':
            print(f"{car.title()} salonda yo'q.")
        else:
            print(f"{car.upper()} salonda yo'q.")
    else:
        print(f"{car.title()} sotib olasizmi?")




















