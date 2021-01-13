'''
# While List
ismlar = []
print("Yaqin do'stlaringiz ro'yhatini tuzamiz.")
n = 1
while True:
    savol = f"{n}-do'stingizni ismini kiriting: "
    ism = input(savol)
    ismlar.append(ism)
    javob = input("Yana ism qo'shasizmi? (ha/yo'q) ")
    if javob == 'ha':
        n += 1
        continue
    else:
        break
print("Do'stlaringiz ro'yhati: ")
for ism in ismlar:
    print(ism.title())
'''
# While Lug'atlar (dict)
print("Do'stlaringizni yoshini saqlaymiz.")
dostlar = {}
ishora = True
while ishora:
    ism = input("Do'stingizni ismini kiriting: ")
    yosh = input(f"{ism.title()}ning yoshini kiriting: ")
    dostlar[ism] = int(yosh)

    javob = input("Yana ma'lumot qo'shasizmi? (ha / yo'q)")
    if javob == "yo'q":
        ishora = False

for ism, yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshda.")