#1
# n = int(input("Juft son kiriting: "))
# if n % 2 == 0:
#     print("Raxmat")
# else:
#     print("Bu juft son emas.")

#2
# yosh = int(input("Yoshingizni kiriting: "))
# if yosh <= 4 or yosh >= 60:
#     print("Sizlarga bepul.")
# elif yosh <= 18:
#     print("Sizlarga kirish 10000 so'm")
# elif yosh >= 18:
#     print("Sizlarga kirish 20000 so'm")

#4
# mahsulotlar = ['anor', 'ruchka', 'muzqaymoq', 'uzum', 'dori', 'olma', 'nok', 'daftar', 'qovun', 'qalam']
# bor_mahsulotlar = []
# mavjud_emas = []
# for i in range(1,6):
#     mahsulot = input(f"Savatga {i}-mahsulotni qo'shing: ")
#     bor_mahsulotlar.append(mahsulot)
# for a in bor_mahsulotlar:
#     if a not in mahsulotlar:
#         mavjud_emas.append(a)
# if mavjud_emas:
#     print("\nQuyidagi mahsulotlar do'konimizda yo'q:")
#     for i in mavjud_emas:
#         print(i)
# else:
#     print("\nSiz so'ragan barcha mahsulotlar do'konimizda bor")

#5
n = int(input("Istalgan butun son kiriting: "))
for i in range(2, 11):
    if n % i == 0:
        print(f"{n} soni {i} ga qoldiqsiz bo'linadi.")