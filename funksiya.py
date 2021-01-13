# def salom_ber(ism):
#     """Salom beruvchi funksiya"""
#     print(f"Salom {ism.title()}!")
# salom_ber('bekzod')

# def havyon(turi, ismi, yoshi = 5):
#     """Hayvon turi va ismini chiqaradi"""
#     print(f"Menda {turi.title()} bor.")
#     print(f"Uning laqabi {ismi.title()}. {yoshi} yoshda.")
# havyon('it', 'simba', 2)
# havyon(ismi = 'shmshillo', turi = 'mushuk')
'''
def get_formatted_name(first_name, last_name, age = ''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
football = get_formatted_name('cristiano', 'ronaldo', 35)
print(football)

def passport(f_name, l_name, age = ''):
    full_name = f"{f_name} {l_name} "
    if age:
        full_name += f'{age} years old.'
    return full_name
while True:
    first = input('Ismingizni kiriting: ')
    last = input('Familyangizni kiriting: ')
    l = input('Yoshingizni ham kiritaszmi? (Yes/No)')
    if l == 'Yes':
        age = input("Yoshingiz nechada: ")
        print(passport(first, last, age))
    else:
        print(passport(first, last))
    p = input("Ma'lumot qo'shaszmi? (Yes/No)")
    if p == 'No':
        break
'''
def fish(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("\nIltimos barchasini to'liq kiriting.")
    f_name = input("Ismingizni kiriting: ")
    l_name = input("Familyangizni kiriting: ")
    print(fish(f_name, l_name))
    x = input("Yana malumot kiritaszmi?(Ha/Yo'q) ")
    if x == "Yo'q":
        break
