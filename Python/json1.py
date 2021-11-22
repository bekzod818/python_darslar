import json

x = 10
x_json = json.dumps(x)

l = ["banana", "apple", "orange", 15]
l_json = json.dumps(l)

ism = "Python"
ism_json = json.dumps(ism)

x = {
  "name": "John",
  "age": 30,
  "city": ["London", "New York", "Moscow"],
  "car": {
      "model": "Malibu",
      "range": "qora",
      "year": 2021
  }
}

x = {
  "name": "Doe",
  "age": 25,
  "city": ["London", "New York", "Moscow"],
  "car": {
      "model": "Gentra",
      "range": "Oq",
      "year": 2019
  }
}
x_json = json.dumps(x, indent=4)

x1 = json.loads(x_json)
# print(x1['city'][1])
# print(type(x1))

# with open("data.json", "r") as file:
#     x1 = file.read()


with open("example_2.json") as file:
    a = json.load(file)
# print(a['quiz'].keys())
print(f"Fanlar: {a['quiz'].keys()}")
print(f"Savollar: {a['quiz']['sport']['q1']['question']}")
print(f"Variantlar: {a['quiz']['sport']['q1']['options']}")
print(f"To'g'ri javob: {a['quiz']['sport']['q1']['answer']}")

print()
print(f"Savollar: {a['quiz']['maths']['q2']['question']}")
print(f"Variantlar: {a['quiz']['maths']['q2']['options']}")
print(f"To'g'ri javob: {a['quiz']['maths']['q2']['answer']}")



# print(x_json)
# print(type(x_json))
# print(ism_json[4])
# print(type(ism_json))
# print(l_json[-1])
# print(type(l_json))