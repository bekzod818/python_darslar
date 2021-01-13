
#1 Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
print('Buyurtmalarni qabul qiluvchi dastur.')
buyurtmalar = []
while True:
    buyurtma = input('Buyurtmangizni kiriting: ')
    if buyurtma == 'exit':
        break
    else:
        buyurtmalar.append(buyurtma)
#print(f'Sizning buyurtmalariz {buyurtmalar}')

mahsulotlar = {'olma': 20000,
               'shaftoli': 25000,
               'tarvuz': 18000,
               'uzum': 22000,
               'qovun': 15000}
while buyurtmalar:
    mahsulot = buyurtmalar.pop()
    if mahsulot in mahsulotlar.keys():
        narx = mahsulotlar[mahsulot]
        print(f'{mahsulot.title()} - {narx} som.')
    else:
        print(f'Bizda {mahsulot} yoq.')