mytuple = ('olma', 'banan', 'olcha')
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Looping Through an Iterator
for x in mytuple:
    print(x)

str = 'apelsin'
myit1 = iter(str)

# Looping Through an Iterator
for i in str:
    print(i)

print(next(myit1))
print(next(myit1))
print(next(myit1))
print(next(myit1))
print(next(myit1))
print(next(myit1))
print(next(myit1))

# Create an Iterator
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

p = MyNumbers()
myiter = iter(p)

print(next(myiter))
print(next(myiter))
print(next(myiter))


# StopIteration
class MyNumber:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
myclass = MyNumber()
myiter1 = iter(myclass)

for x in myiter1:
    print(x)
