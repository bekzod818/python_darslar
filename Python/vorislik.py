from classlar import Shaxs

class Talaba(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, guruh, yonalish):
        super().__init__(ism, familiya, passport, tyil)
        self.guruh = guruh
        self.yonalish = yonalish
        self.fanlar = []
    
    def get_info(self): 
        return f"Ism: {self.ism}, Familiya: {self.familiya}, Passport: {self.passport}, Tug'ilgan yil: {self.tyil}\nTalabaning guruhi: {self.guruh}, Yo'nalishi: {self.yonalish}\n"

    def fanga_yozil(self, *fan):
        for i in fan:
            self.fanlar.append(i)

    def get_fanlar(self):
        return self.fanlar
        


# talaba1 = Talaba("Feruz", "Karimov", "AC12395945", 2002, 802, "Python")
# talaba2 = Talaba("Amirbek", "Ibragimov", "AB62839594", 2007, 801, "Python")

# print(talaba1.get_info())
# print(talaba2.get_info())

    
