"""
mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
#mehmonlar.sort(reverse=True)
print(sorted(mehmonlar, reverse=True))

sonlar = [1, 2, 3, 4, 5]
sonlar2 = sonlar[:]
sonlar.append(0)
sonlar.extend([6,-7,-8,9])
sonlar2.remove(1)
sonlar2.insert(2,-7)
print(sonlar)
print(sonlar2)

davlatlar = ["Uzbekistan", "Spain", "Italy", "Portugal", "Russia"]
#print(len(davlatlar))
print(sorted(davlatlar, reverse=True))
davlatlar.reverse()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

juft = list(range(120, 1200, 2))
print(sum(juft), max(juft) - min(juft), len(juft))
print(juft[:21])
print(juft[520:])
x = len(juft)
y = int(x/2 - 10)
z = int(x/2 + 10)
print(juft[y:z])
"""

taomlar = ["kabob", "somsa", "tuxum", "manti", "qatlama"]
nonushta = taomlar[:]
nonushta.remove("kabob")
nonushta.remove("somsa")
nonushta.remove("manti")
nonushta.append("saryog'")
nonushta.append("murabbo")
taomlar.append("barak")
taomlar.remove("tuxum")
nonushta = tuple(nonushta)
print(taomlar)
print(nonushta)