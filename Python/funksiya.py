def jarima(tezlik):
    """Bu funksiya jarimani aniqlaydi"""
    if 75 < tezlik <= 90:
        return 1
    elif 90 < tezlik <= 110:
        return 5
    elif 110 < tezlik <= 130:
        return 10
    elif tezlik > 130:
        return 20
    else:
        return 'yo\'q'


car1 = jarima(70)
car2 = jarima(85)
car3 = jarima(99)
car4 = jarima(150)
print(f"Jarima {car1}.")
print(f"Jarima {car2} EKIH.")
print(f"Jarima {car3} EKIH.")
print(jarima.__doc__)








def chegirma(yosh):
    """Bu funksiya chegirmani aniqlaydi"""
    pass


"""
1 - 12 yoshgacha 50% chegirma
13 - 18 yoshgacha 40% chegirma
19 - 60 yoshgacha 30% chegirma
61 - ... yoshgacha 50% chegirma
"""



# def juft_toq(num):
#     if num % 2 == 0:
#         return 'Juft son'
#     else:
#         return 'Toq son'


# n = int(input('Son kiriting: '))

# print(juft_toq(n))









# def full_name(first_name, last_name):
#     return f"Mening to'liq ismim {first_name} {last_name}"


# x = full_name('Bekzod', 'Raximov')
# print(x)
# y = full_name('Bexruz', 'Aminboyev')
# print(y)


# print(full_name('Bekzod', 'Raximov'))






# def salom(name):
#     print(f'Salom {name}')

# salom('Umar')
# salom('Komil')
# salom('Lobar')

# ism = 'Javohir'
# print(f"Salom -> {ism}")
