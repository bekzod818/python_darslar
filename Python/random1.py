from random import randint, randrange, choice, shuffle

l = ["Bexruz", "Shoxmalik", "Og'abek", "Amirbek", "Mardon"]
# s = "Python zor dasturlash tili"
# tasodifiy_son = randint(1, 100)
# tasodifiy_son = randrange(100)
# print(tasodifiy_son)
l1 = list(range(0, 100, 2))
tasodifiy_son = choice(l1)
ismlar = l[:]
# print(tasodifiy_son)
shuffle(l)
print(ismlar)
print(l)