ismlar = ['doniyor', 'bekzod', 'javlon']
for ism in ismlar:
    print(f"Salom {ism.title()} yaxshimisan.")
mashinalar = ['malibu', 'cobalt', 'audi']
for mashina in mashinalar:
    print(f"Men {mashina.title()}ga ega bo'lishni hohlayman.")

shaxslar = ["ronaldo", "aziz estet", "bekzod"]
print(f"{shaxslar[2].title()} mehmonga kela olmaydi")
shaxslar[2] = 'katrina kaif'
for shaxs in shaxslar:
    print(f"{shaxs.title()} sizni kechki ovqatga taklif qilaman.")
print(shaxslar)

travel = ['new york', 'dubai', 'london', 'madrid', 'paris']
print(sorted(travel, reverse=True))
travel.reverse()
print(travel)
travel.sort()
print(travel)
travel.sort(reverse=True)
print(travel)
print(len(travel))
