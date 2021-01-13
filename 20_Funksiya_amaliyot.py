"""
def data(first_name, last_name, birth_year, adress, email, tel_number):
    data = {
        'first_name': first_name,
        'last_name': last_name,
        'birth_year': birth_year,
        'adress': adress,
        'email': email,
        'tel_number': tel_number
    }
    return data
mijozlar = []
while True:
    print("Ma'lumotlaringizni kiriting.")
    first_name = input('Ismni kiriting: ')
    last_name = input('Familyani kiriting: ')
    birth_year = input("Tug'ilgan yilni kiriting: ")
    adress = input('Manzilni kiriting: ')
    email = input('Elektron pochtani kiriting: ')
    tel_number = input('Telefon raqam kiriting: ')
    mijozlar.append(data(first_name, last_name, birth_year, adress, email, tel_number))
    javob = input("Yana qo'shasizmi? (yes/no): ")
    if javob == 'no':
        break

for data in mijozlar:
    print('--------------------------------------------------------------')
    print(f"To'liq ismi {data['last_name']} {data['first_name']}, Yoshi {2020 - int(data['birth_year'])} da.")
    print(f"Manzili {data['adress']}, elektron pochtasi {data['email']}, telefon raqami {data['tel_number']}")

def maks(num1, num2, num3):
    if num1 >= num2 >= num3 or num1 >= num3 >= num2:
        maksimal = num1
    elif num2 >= num1 >= num3 or num2 >= num3 >= num1:
        maksimal = num2
    elif num3 >= num1 >= num2 or num3 >= num2 >= num3:
        maksimal = num3
    return maksimal
print(maks(-3, -6, 0))

malumot = []
def doira(r):
    circle = {
        'radius': radius,
        'diametr': 2 * radius,
        'uzunlik': 2 * 3.14 * radius,
        'yuz': 3.14 * radius * radius
    }
    return circle

radius = int(input('Radiusni kiriting: '))
print(doira(radius))
"""
def fibonachi(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonachi(n - 2) + fibonachi(n - 1)
x = int(input())
for i in range(1, x + 1):
    print(fibonachi(i))