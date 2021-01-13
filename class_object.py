class Person():
    def __init__(self, f_name, l_name):
        self.firstname = f_name
        self.lastname = l_name
    def full_name(self):
        print(f"{self.firstname} {self.lastname}")
    
class Child(Person):
    def __init__(self, f_name, l_name, b_year):
        super().__init__(f_name, l_name)
        self.birth_year = b_year
    def data(self):
        print(f"{self.firstname} {self.lastname} {2030 - self.birth_year} yoshda.")

p1 = Person('Bekzod', 'Raximov')
p1.full_name()
p1.firstname = 'Asadbek'
p1.full_name()
p2 = Child('Bexruz', 'Sotimov', 2008)
p2.lastname = 'Raximov'
p2.data()
print(str(p2.birth_year) + '-yilda tugilgan.')
p3 = Child('Parizoda', 'Dilshodova', 2025)
p3.data()
print(str(p3.birth_year) + '-yilda tugilgan.')
