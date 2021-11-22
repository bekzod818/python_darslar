import json

data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}

data_json = json.dumps(data)

talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""

with open("talaba.json", "w") as file:
    json.dump(talaba_json, file)


with open("data1.json", "w") as file:
    json.dump(data_json, file)

print(data_json)
print(talaba_json)