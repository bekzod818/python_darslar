class Person:
    # Konstruktor
    def __init__(self, ism):
        self.ism = ism

    # def __del__(self):
    #     print(self.ism, 'Xotiradan o\'chdi')

    # Metod
    def display_info(self):
        print(f"Salom, mening ismim {self.ism}")

class Auto:
    def __init__(self, name):
        self.name = name

    def move(self, speed):
        print(f"{self.name} - {speed} km/soat tezlik bilan harakatlanyabdi.")


"""
# Obyekt
p1 = Person('Ali') # 1-obyekt
p1.display_info() # metod
del p1 # 1-obyektni o'chirish

p2 = Person('Salim') # 2-obyekt
p2.display_info() # metod
"""
