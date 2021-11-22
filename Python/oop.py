class Talaba:
    """Talabalarni klassi"""
    def __init__(self, ism, familiya, yosh):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh
        self.bosqich = 1

    def get_full(self):
        return f"{self.ism} {self.familiya} {self.yosh} yoshda. {self.bosqich} bosqichda o'qiydi"

    def b_year(self, c_year):
        return f"{self.ism} {c_year - self.yosh}-yilda tug'ilgan."

    def set_bosqich(self, bosqich):
        self.bosqich = bosqich
        return self.bosqich


talaba1 = Talaba("Bekzod", "Raximov", 21)
# talaba1.ism = "Jamol"
# talaba1.bosqich = 4
talaba2 = Talaba("Behruz", "Aminboyev", 16)

print(talaba1.familiya)
# print(talaba2.b_year(2021))
print(talaba1.get_full())

print(talaba1.set_bosqich(4))

print(talaba1.__dict__)