"""
# Dictionary - Lug'at 
car = {
    'brend': 'chevrolet',
    'model': 'malibu',
    'yili': 2020,
    'korobka': 'avtomat'
}
car['narh'] = 35000
car['rang'] = 'qora'
car['korobka'] = 'mexanik'
del car['yili']
print(car)
print(car['model'].title())

favorite_lang = {
    'doniyor': 'c++',
    'javlon': 'php',
    'bekzod': 'python',
    'ulugbek': 'java',
    'nurik': 'js',
    'sher': 'c++',
    'zafar': 'python'
}
friends = ['javlon', 'nurik', 'sher']
programmers = []
for x, y in favorite_lang.items():
    print(f"{x.title()}'s favorite language is {y.upper()}")
for x in favorite_lang.keys():
    programmers.append(x.title())
print(f"Programmers: {programmers}")
for x in friends:
    if x in favorite_lang.keys():
        print(f"{x.title()} is my friend.")
for name in sorted(favorite_lang.keys()):
    print(f"{name.title()} is developer.")
for lang in set(favorite_lang.values()):
    print(lang.upper())

# Nesting
malibu = {
    'narx': 35500,
    'rang': 'qora',
    'korobka': 'avtomat'
}
cobalt = {
    'narx': 10500,
    'rang': 'oq',
    'korobka': 'mexanik'
}
damas = {
    'narx': 7500,
    'rang': 'molochniy',
    'korobka': 'mexanik'
}
mashinalar = [malibu, cobalt, damas]
for mashina in mashinalar:
    print(mashina)

cars = []
for i in range(30):
    car = {
        'brend': 'chevrolet',
        'model': None,
        'korobka': 'mexanik',
        'yil': 2020
    }
    cars.append(car)

for car in cars[:3]:
    car['model'] = 'malibu'
    car['korobka'] = 'avtomat'

for car in cars[:6]:
    if car['korobka'] == 'mexanik':
        car['model'] = 'cobalt'
    print(car)
print(f"Barcha mashinalar {len(cars)} ta.")

developer = {
    'name': 'bekzod',
    'lang': ['c++', 'python', 'js'],
    'age': 20
}
print(f"{developer['name'].title()} is 20 years old.")
print("Your favorite languages: ")
for a in developer['lang']:
    print(f'\t{a.upper()}')

favorite_lang1 = {
    'jen': ['python', 'ruby', 'java'],
    'sarah': ['c#', 'c++'],
    'edward': ['ruby', 'go', 'js'],
    'phil': ['python', 'php'],
}
for key, value in favorite_lang1.items():
    print(f"{key.title()}'s favorite languages:")
    for i in value:
        print(f"\t{i.upper()}")
    print("-----------------------------------")
"""
footballer = {
    'CR7': {
        'first': 'cristiano',
        'last': 'ronaldo',
        'location': 'portugal',
    },
    'LM10': {
        'first': 'lionel',
        'last': 'messi',
        'location': 'argentina',
    }
}
for name, info in footballer.items():
    print(f"The best player in the world {name}")
    full_name = info['first'] + " " + info['last']
    location = info['location']
    print(f"Name: {full_name.title()}. From: {location.title()}")
    print("-" * 35)









































