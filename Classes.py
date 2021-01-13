class Person:
    # Konstruktor
    def __init__(self, name, year):
        self.name = name
        self.year = year
    # Destruktor
    def __del__(self):
        print(self.name, "Xotiradan o'chdi.")
    # Metod
    def info(self):
        print(f"{self.name} {self.year} yilda tug'ilgan.")
    def age(self):
        age = 2021 - self.year
        print(f"{self.name} {age} yoshga kirdi.")

person1 = Person('Ali', 1998)
person1.name = 'Sherali'
person1.info()
person1.age()
person2 = Person('Jasur', 2000)
person2.year = 2002
person2.info()
person2.age()