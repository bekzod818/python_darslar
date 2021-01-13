# ismlar = ['Sardor', "Vali", "Xasan", 'Doniyor', 'Javlon']
# cnt = 0
# for ism in ismlar:
#     print(f"Salom {ism}")
#     cnt += 1
# print(f"Sikl {cnt} marta takrorlandi")

# numbers = list(range(11, 100, 2))
# for number in numbers:
#     print(number ** 3)

# kinolar = []
# for i in range(5):
#     kino = input(f"{i + 1} - kinoni kiriting: ")
#     kinolar.append(kino)
# print(f"Men yoqtirgan kinolar: {kinolar}")

suhbatdoshlar = []
n = int(input("Bugun necha odam bilan suhbatlashdingiz: "))
for i in range(n):
    suhbatdosh = input(f"{i + 1} - suhbat qurgan odamingiz: ")
    suhbatdoshlar.append(suhbatdosh)
print(suhbatdoshlar)
