#1 Sonlarni ko'paytmasini chiqarsin
def kopaytma(*sonlar):
    p = 1
    for son in sonlar:
        p *= son
    return p
print(kopaytma(1, 2, -3))
print(kopaytma(-5, 0, 5))

# Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.
def talabalar(ism, familiya, **talaba):
    talaba["ism"] = ism
    talaba["familiya"] = familiya
    return talaba
talaba = talabalar("Bekzod", "Raximov", tyil = 2020, kurs = 3, fakultet = "Axborot Xavfsizligi")
print(talaba)