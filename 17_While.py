# input
'''
ism = input('Ismingizni kiriting: ')
savol = f'Salom {ism.title()}. Yoshingiz nechida? '
yosh = input(savol)
yosh = int(yosh)
height = input('Bo\'yingiz necha metr? ')
height = float(height)
print(f'Ism : {ism.title()} Yosh: {yosh} Boyi: {height}')

# while
# son = 1
# while son <= 5:
#     print(son, end=' ')
#     son += 1

print('Kiritilgan sonning kvadratini qaytaruvchi dastur.')
savol = 'Istalgan son kiriting '
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
qiymat = ''
while qiymat != 'exit':
    qiymat = input(savol)
    if qiymat != 'exit':
        print(float(qiymat) ** 2)

print('Yoshingizni hisoblovchi dastur!')
savol = "Tug'ilgan yilingizni kiriting "
savol += "('exit'): "
ishora = True
while ishora:
    t_yil = input(savol)
    if t_yil == 'exit':
        ishora = False
    else:
        print(f'Siz {2020 - int(t_yil)} yoshdasiz.')

print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
while True:
    qiymat = input(savol)
    if qiymat == 'exit':
        break
    else:
        print(int(qiymat) ** 2)

sonlar = list(range(1,11))
for son in sonlar: 
    if son == 5: # son 5 ga teng bo'lsa kod to'xtaydi
        break
    print(f"{son} ning kvadrati {son**2} ga teng")
'''
son = 0
while son < 10:
    son += 1
    if son % 2 != 0:
        continue
    else:
        print(son)







