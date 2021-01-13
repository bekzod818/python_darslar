class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(1, 150):
            self.__age = age
        else:
            print("Mumkin bo'lmagan yosh.")

    @property
    def name(self):
        return self.__name

    def data(self):
        print(f"\nName: {self.__name} Age: {self.__age}")

class Employee(Person):
    def __init__(self, name, age, company):
        Person.__init__(self, name, age)
        # super().__init__(name, age)
        self.age = 23
        self.company = company

    def data(self):
        print(f"{self.name} {self.company}da ishlaydi.")

class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university
    def data(self):
        print(f"Name: {self.name} Age: {self.age} {self.university}da o'qiydi")

people = [Person('Azam', 26), Employee('Jasur',23, 'Googe'), Student('Bekzod', 21, 'TATU UF')]
for person in people:
    # person.data()
    # print()
    if isinstance(person, Student):
        print(person.university)
    elif isinstance(person, Employee):
        print(person.company)
    else:
        print(person.name)

