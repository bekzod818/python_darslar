# 1. Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating
'''
print('Yaxshi ko\'rgan kitoblaringizni kiriting.')
kitoblar = ''
lst = []
while True:
    kitoblar = input()
    if kitoblar == 'stop':
        break
    else:
        lst.append(kitoblar)
print(f'Men yoqtirgan kitoblar {lst}')

# 2. Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).
print('Muzeyimizga xush kelibsiz!')
savol = 'Yoshingizni kiriting? '
yosh = ''
while True:
    yosh = input(savol)
    if yosh == 'exit' or yosh == 'quit':
        break
    elif int(yosh) < 7:
        narx = 2000
        print(f"Chipta narxi {narx} som")
    elif 7 <= int(yosh) <= 18:
        narx = 3000
        print(f"Chipta narxi {narx} som")
    elif 18 <= int(yosh) <= 65:
        narx = 10000
        print(f"Chipta narxi {narx} som")
    else:
        print('Sizlarga bepul (=)')
'''
# 3 Quyidagi dasturda bir nechta mantiqiy xatolar bor. Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib qolmoqda. Xatolarni to'g'rilay olasizmi?
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat == 'exit':
        break
    elif float(qiymat)<0:
        continue # agar foydalanuvchi manfiy son kiritsa tsiklni takrorlaymiz
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")