l = [1, 5, 10, 25]

try:
    print(l[5])
except Exception as e:
    print("Xatolik", e)
else:
    print("Element chiqarildi")
finally:
    print("Dastur tugadi")














# try:
#     # print(x)
#     print(2 / 1)
# except NameError:
#     print("Siz x ni elon qilmagansiz")
# except ZeroDivisionError:
#     print("Nolga bo'lish mumkin emas")
# else:
#     print("Xatolik yuz bermadi")
# finally:
#     print("Dastur tugadi")
