def fish(ism, familya, otasining_ismi = ''):
    if otasining_ismi:
        return f'{ism} {otasining_ismi} {familya}'
    else:
        return f'{ism} {familya}'
talaba1 = fish('Olim', 'Hakimov', 'Abrorovich')
talaba2 = fish('Hakim', 'Olimov')
print(f"Bugun darsga kelmaganlar: {talaba1} va {talaba2}")

# Funksiyadan lu'gat qaytaramiz
def avto_info(kompaniya, model, rangi, korobka, yili, narhi = None):
    avto = {
        'kompaniya': kompaniya,
        'model': model,
        'rang': rangi,
        'korobka': korobka,
        'yil': yili,
        'narh': narhi
    }
    return avto
avto1 = avto_info('GM', 'Malibu', 'Qora', 'avtomat', 2018)
avto2 = avto_info('GM', 'Cobalt', 'Oq', 'mexanik', 2019, 10000)
avtolar = [avto1, avto2]
while True:
    print('Quyidagi malumotlarni kiriting')
    kompaniya=input("Ishlab chiqaruvchi: ")
    model=input("Modeli: ")
    rangi=input("Rangi: ")
    korobka=input("Korobka: ")
    yili=input("Ishlab chiqarilgan yili: ")
    narhi=input("Narhi: ")
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    javob = input("Yana qo'shasizmi? (yes/no): ")
    if javob == 'no':
        break

print('Onlayn bozordagi mavjud avtomashinalar:')
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = "No'malum"
    print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")

# Funksiyadan ro'yhat qaytaramiz
def oraliq(min, max, qadam = ''):
    sonlar = []
    if qadam:
        qadam = int(qadam)
        while min < max:
            sonlar.append(min)
            min += qadam
    else:
        while min < max:
            sonlar.append(min)
            min += 1
    return sonlar
print(oraliq(1,11), oraliq(0,21,2))


