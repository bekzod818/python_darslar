# *args Usuli
def summa(*sonlar):
    """Sonlarni yig'indisini hisoblavchi"""
#    return sum(sonlar)
    summa = 0
    for son in sonlar:
        summa += son
    return summa
# print(summa(1,2,3))
# print(summa(4, -7, 2))

def ifoda(x, y, *sonlar):
    """Ifodani hisoblaydi"""
    return sum(sonlar) * (x ** y)
# print(ifoda(2, 3, 4, 5, -8, 1))
# print(ifoda(1,2))

# **kwargs Usuli (keywords arguments)
def avto_info(kompaniya, model, **malumotlar):
    malumotlar["kompaniya"] = kompaniya
    malumotlar["model"] = model
    return malumotlar
avto1 = avto_info("GM", "Malibu", rang = "qora", yil = 2018)
avto2 = avto_info("Kia", "K5", rang = "qizil", narx = 35000, korobka = "avtomat")
print(avto1)
print(avto2)