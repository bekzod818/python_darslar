'''
#1 Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
def t_yil(ism, yosh):
    """Tug'ilgan yilingizni hisoblovchi funksiya"""
    joriy_yil = 2020
    javob = f'Siz {joriy_yil - yosh}-yilda tugilgansiz.'
    return javob
print(t_yil('Bekzod',20))

#2 Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
def kv_kub(son):
    print(f'{son} ning kvadrati {son ** 2}')
    print(f'{son} ning kubi {son ** 3}')
n = int(input('Son kiriting: '))
kv_kub(n)

#3 Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
def odd_even(son):
    if son % 2 == 0:
        print(f'{son} juft son.')
    else:
        print(f'{son} toq son.')
while True:
    n = input('Son kiriting: ')
    if n == 'exit':
        break
    else:
        odd_even(int(n))

#4 Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
def maks(son1, son2):
    if son1 > son2:
        print(f'{son1} katta {son2} dan')
    elif son1 == son2:
        print('Sonlar teng.')
    else:
        print(f'{son1} kichik {son2} dan')
def daraja(x, y = 2):
    return pow(x, y)
a, b = map(int, input().split())
maks(a, b)
print(daraja(a))

#5 Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.
def bolinish(son):
    for i in range(2, 10):
        if son % i == 0:
            print(f'{son} soni {i} ga qoldiqsiz bolinadi')
n = int(input())
bolinish(n)


def tub_son(num):
	ishora = True
	i = 2
	while i < num / 2:
		if num % i == 0:
			ishora = False
			break
		i += 1
	return ishora

tub_sonlar = []
a, b = map(int, input('Oraliqni kiriting: ').split())
for i in range(a, b + 1):
	if tub_son(i):
		tub_sonlar.append(i)

print(f"{a} va {b} oraliqdagi tub sonlar: {tub_sonlar}")
'''


