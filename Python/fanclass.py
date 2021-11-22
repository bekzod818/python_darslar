from vorislik import Talaba

class Fan:
    def __init__(self, nomi, oqtuvchi, talaba_soni):
        self.nomi = nomi
        self.oqtuvchi = oqtuvchi
        self.talaba_soni = talaba_soni
    
    def get_nomi(self):
        return f"{self.nomi}"

fan1 = Fan("Matematika", "Mamedov Qudrat", 20)
fan2 = Fan("Fizika", "Sadullayev Shuhrat", 18)
fan3 = Fan("Ingliz tili", "Muhammedov Maqsud", 21)


talaba1 = Talaba("Feruz", "Karimov", "AC12395945", 2002, 802, "Python")
talaba2 = Talaba("Amirbek", "Ibragimov", "AB62839594", 2007, 801, "Python")

talaba1.fanga_yozil(fan1.get_nomi(), fan3.get_nomi())
talaba2.fanga_yozil(fan2.get_nomi(), fan3.get_nomi())
print(talaba1.get_fanlar())
print(talaba2.get_fanlar())
