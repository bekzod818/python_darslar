"""
talaba = {
    'familiya': 'Raximov',
    'ism': 'Bekzod',
    'yosh': 20
}
print(f"{talaba['familiya'].title()} {talaba['ism'].title()} {talaba['yosh']} yoshda")
talaba['kurs'] = 3
talaba['fakultet'] = 'Axborot Xavfsizlik'
print(f"U hozir {talaba['fakultet']} yo'nalishida {talaba['kurs']} kursda o'qiydi.")

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }
phone = telefonlar.get('olim', "Bunday foydalanuvchi yo'q")
print(phone)
"""

#AMALIYOT

buvi = {
    'ism': 'Ovadan',
    't_yil': 1951,
    'kasb': 'nafaqaxo\'r'
}
ota = {
    'ism': 'Dilshod',
    't_yil': 1975,
    'kasb': 'hisobchi'
}
ona = {
    'ism': 'Nazokat',
    't_yil': 1978,
    'kasb': 'o\'qituvchi'
}
print(f"Buvimning ismi {buvi['ism']}. {buvi['t_yil']}-yilda tug'ilgan. Hozirda {buvi['kasb']}.")
print(f"Otamning ismi {ota['ism']}. {ota['t_yil']}-yilda tug'ilgan. Hozirda {ota['kasb']}.")
print(f"Onamning ismi {ona['ism']}. {ona['t_yil']}-yilda tug'ilgan. Hozirda {ona['kasb']}.")

sevimli_taomlar = {
    'buvim': 'gumma',
    'otam': 'barak',
    'onam': 'palov',
    'ukam_1': 'gosht',
    'ukam_2': 'manti'
}
for x, y in sevimli_taomlar.items():
    print(f"{x.title()}ning sevimli ovqati {y}.")

python = {
    'int': 'butun sonlar',
    'float': 'Haqiqiy sonlar',
    'complex': 'Kompleks sonlar',
    'str': 'Matn yoki harflar',
    'if': 'Shart operatori',
    'for': 'Takrorlanuvchi operator',
    'bool': 'Mantiqiy qiymat qaytaradi',
    'list': 'Ro\'yhat',
    'tuple': 'Kortej',
    'dict': 'Lug\'at'
}
a = input('Nima bilmoqchisiz: ')
b = python.get(a)
if b == None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{a.title()} => {b}")