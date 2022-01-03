dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
dict3 = {**dict1, **dict2}

# print(dict1)
# print(dict3)

sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sample_dict.values():
    print("200 soni bor")
else:
    print("200 soni yo'q")



sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}













# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# # Keys to extract
# keys = ["name", "salary"]

# newdict = {}
# for i in sample_dict:
#     if i not in keys:
#         newdict[i] = sample_dict[i]

# print(newdict)