def age(t_yil, j_yil=2021):
    yosh = j_yil - t_yil
    return yosh

print(age(2000))










# def age(**kwargs):
#     yosh = 2021 - kwargs["t_yil"]
#     return yosh

# def fullname(**data):
#     s = f"{data['fname']} {data['lname']}"
#     return s


# print(age(fname="Bekzod", lname="Raximov", t_yil=2000))
# print(fullname(fname="Bekzod", lname="Raximov", t_yil=2000))











# def perimetr(a, b, c):
#     p = a + b + c
#     return p


# print(perimetr(1,2,3))












# def summa(son, *sonlar):
#     s = 0
#     for i in sonlar:
#         s += i
#     return s + son


# print(summa(2,3))











# def family(*child):
#     f = "Sharipov"
#     for i in child:
#         print(f"{i} {f}")

# family("G'ulom", "Karim")
















# def daraja(a, b):
#     p = 1
#     for i in range(b):
#         p *= a
#     return p

# def fullname(firstname, lastname):
#     s = f"{firstname.title()} {lastname.title()}"
#     return s


# print(fullname("bekzod", "RAXIMOV"))


# fn = fullname("Jasur", "Karimov")














# x = daraja(2, 3)

# print(x + 5)







# def factorial(num):
#     p = 1
#     for i in range(1, num + 1):
#         p *= i
#     return p

# print(factorial(2))
















# def jufttoq(a):
#     if a % 2 == 0:
#         return "Juft"
#     else:
#         return "Toq"


# x = jufttoq(8)

# print(x)
















# def salom_ber(name):
#     print(f"Salom {name}")



# salom_ber("Sardor")
# salom_ber("Hurmat")
# salom_ber("Jurat")