"""
class Person:
    def __init__(self, name):
        self.__name = name
        self.__age = None
    def set_age(self, age):
        if age in range(1,150):
            self.__age = age
        else:
            print("Mumkin bo'lmagan yosh")
    def get_age(self):
        return self.__age
    def get_name(self):
        return self.__name
    def info(self):
        print(f"{self.__name} {self.__age} yoshda")

person1 = Person('Shodlik')
person1.set_age(15)
person1.info()
person2 = Person('Feruz')
person2.set_age(23)
person2.info()
"""

class Odam():
    def __init__(self, ism, yosh):
        self.__ism = ism
        self.__yosh = yosh
        self.jins = ''

    def malumot(self):
        print(f"Ismi: {self.__ism} \nYoshi: {self.__yosh}")

    def set_yosh(self, yosh):
        if yosh in range(1, 150):
            self.__yosh = yosh
        else:
            print("Mumkin bo'lmagan yosh.")

    def get_yosh(self):
        return self.__yosh

    def set_ism(self, ism):
        self.__ism = ism

    def get_ism(self):
        return self.__ism

odam1 = Odam('Bekzod', 20)
odam1.set_yosh(25)
odam1.set_ism('Temur')
odam1.jins = 'Erkak'
odam1.malumot()
print(f"Jinsi: {odam1.jins}")


class Person():
    def __init__(self, name):
        self.__name = name
        self.__age = None

    @property # get_age
    def age(self):
        return self.__age

    @age.setter # set_age
    def age(self, age):
        if age in range(1, 150):
            self.__age = age
        else:
            print("Mumkin bo'lmagan yosh.")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def data(self):
        print(f"Name: {self.__name} \nAge: {self.__age}")

    def __str__(self):
        return f"Name: {self.__name} \nAge: {self.__age}"

person1 = Person('Jack')
person1.age = 21
person1.data()
person1.name = 'Bob'
person1.data()
print("-"*25)
print(person1)













