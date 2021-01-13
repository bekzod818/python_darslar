# from modul import avto_info as ainfo, avto_kirit
# import modul as mod

# avto1 = ainfo("GM", "Malibu", "Qora", "avtomat", 2020, 40000)
# mod.info_print(avto1)
# print(mod.p)

# from math import exp, sin, atan, log2, ceil
# x = int(input("Son kiriting: "))
# y = ceil(x * exp(x) * sin(x) / atan (x) + log2(x * x))
# print("%.2f" % y)

from random import randint, choice, shuffle
x = randint(1, 100)
print(x)
lst = ['beko', 'joni', 'doni', 'sher']
c = choice(lst)
print(c)
print(choice(c))
l = list(range(10, 50, 5))
print(l)
shuffle(l)
print(l)