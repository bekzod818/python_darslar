"""
import math
uzunlik = lambda pi, r: 2 * pi * r
print(uzunlik(math.pi, 10))

daraja = lambda x, y: x ** y
print(daraja(2, 10))

def daraja(n):
    return lambda x: x ** n
kvadrat = daraja(2)
kub = daraja(3)
n = int(input('a = '))
print(f"{n} ning kvadrati {kvadrat(n)}, kubi esa {kub(n)}")

from math import sqrt
sonlar = list(range(11))
ildizlar = list(map(sqrt, sonlar))
print(sonlar)
print(ildizlar)

def daraja3(son):
    return son ** 3
sonlar = list(range(11))
print(list(map(daraja3, sonlar)))

kvadratlar = list(map(lambda x: x * x, sonlar))
print(kvadratlar)

a = [4, 5, 6]
b = [7, 8, 9]
# print([x + y for x, y in zip(a, b)])
a_plus_b = list(map(lambda x, y: x + y, a, b))
print(a_plus_b)

ismlar = ['hasan', 'husan', 'olim', 'umid']
print(list(map(lambda matn: matn.upper(), ismlar)))
"""
import random as r
sonlar = r.sample(range(100), 10)

# def juftmi(x):
#     return x % 2 == 0

# juft_sonlar = list(filter(juftmi, sonlar))
juft_sonlar = list(filter(lambda x: x % 2 == 0, sonlar))
print(sonlar)
print(juft_sonlar)

mevalar = ['olma', 'anor', 'anjir', 'shaftoli',
           "o'rik", "tarvuz", "qovun", "banan"]
mevalar_b = list(filter(lambda matn: matn.startswith('b'), mevalar))
print(mevalar_b)

mevalar2 = list(filter(lambda meva: len(meva) <= 5, mevalar))
print(mevalar2)

mevalar1 = list(filter(lambda matn: matn.startswith('a') and matn.endswith('r'), mevalar))
print(mevalar1)





