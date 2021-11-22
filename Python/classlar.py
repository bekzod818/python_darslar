class Avto:
    def __init__(self, model, rang, korobka, narh):
        self.model = model
        self.color = rang
        self.box = korobka
        self.price = narh
        self.kilometr = 0
    
    def set_kilometr(self, km):
        self.kilometr = km
    
    def get_info(self):
        return f"Modeli: {self.model}, Rangi: {self.color}, Korobka: {self.box}\nNarhi: {self.price} $, Kilometr: {self.kilometr} km"


avto1 = Avto("Malibu", "qora", "avtomat", 30000)
avto1.set_kilometr(1000)

avto2 = Avto("Cobalt", "Oq", "mexanik", 10000)
avto2.set_kilometr(12500)

avto3 = Avto("Gentra", "Moviy", "avtomat", 15000)
avto3.set_kilometr(25025)

# print(avto1.get_info())
# print(avto2.get_info())
# print(avto3.get_info())
# print(avto1.__dict__)
# print(avto2.__dict__)
# print(avto3.__dict__)


class Shaxs:
    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.__tyil = tyil

    def get_info(self):
        return f"Ism: {self.ism}, Familiya: {self.familiya}, Passport: {self.passport}, Tug'ilgan yil: {self.__tyil}"

    def get_tyil(self):
        return self.__tyil
    
    def set_tyil(self, yil):
        self.__tyil = yil

inson1 = Shaxs("Karimboy", "Fozilov", "AB1234567", 1999)
inson1.set_tyil(2001)
print(inson1.get_info())
