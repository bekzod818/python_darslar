"""
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
}
# y = thisdict['narx']
x = thisdict.get('narx')
# thisdict['model'] = 'Hyundai'
# thisdict['year'] = 2020
# print(f"Brand - {thisdict['brand']}")
# print(thisdict['model'])
# print(thisdict['year'])
# print(x)
thisdict['color'] = 'White'
# print(thisdict.keys())
# print(thisdict.values())
# print(thisdict.items())
thisdict.update({'color': 'Black'})
thisdict.update({'price': 15000})
# thisdict.pop("brand")
# del thisdict['year']
# print(thisdict)

# for x, y in thisdict.items():
#     print(f"{x} - {y}")

mydict = thisdict.copy()
print(mydict)
"""

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} 
# print(myfamily['child1']['name'])
# print(2021 - myfamily['child2']['year'])
# print(myfamily['child3'])

# x = ('key1', 'key2', 'key3')
# y = 0

# thisdict = dict.fromkeys(x, y)
# print(thisdict)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)
x = car.setdefault("model", "Bronco")

print(x)
print(car)