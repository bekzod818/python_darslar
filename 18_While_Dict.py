'''
print("Do'stlaringizni yoshini saqlaymiz")
dostlar = {}
ishora = True
while ishora:
    ism = input("Do'stingiz ismini kiriting: ")
    yosh = input(f"{ism.title()}ning yoshini kiriting: ")
    dostlar[ism] = int(yosh)

    javob = input("Yana ma'lumot kiritishni hohlayszmi? (ha/yo'q)")
    if javob == "yo'q":
        ishora = False
for ism, yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshda.")

cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
while 'nexia' in cars:
    cars.remove('nexia')
print(cars)
'''
talabalar = ['hasan', 'husan', 'olim', 'botir']
baholangan = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosi: ")
    print(f"{talaba.title()} baholandi!")
    baholangan[talaba] = int(baho)
print()
for talaba, baho in baholangan.items():
    print(f"{talaba.title()} ning bahosi {baho}")
