class Avto:
    """Bu avtomobillar klassi"""
    __num_avto = 0
    def __init__(self, make, model, rang, yil):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        Avto.__num_avto += 1

    # def __str__(self) -> str:
    #     return f"{self.make} {self.model} {self.rang} {self.yil}"

    def __repr__(self) -> str:
        return f"{self.make} {self.model} {self.rang} {self.yil}"

    def __lt__(self, new_avto: object) -> bool:
        return self.yil < new_avto.yil

    def __gt__(self, new_avto: object) -> bool:
        return self.yil > new_avto.yil
    
    def __eq__(self, new_avto: object) -> bool:
        return self.yil == new_avto.yil

    def __ne__(self, new_avto: object) -> bool:
        return self.yil != new_avto.yil


avto1 = Avto("GM", "Malibu", "Oq", 2021)
avto2 = Avto("GM", "Cobalt", "Qora", 2019)
print(Avto.__doc__)
print(dir(Avto))
# print(avto2)