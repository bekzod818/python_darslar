inson = {
    'ism': "Bekzod",
    "familiya": "Raximov",
    "yosh": 21,
    "millat": "o'zbek",
    "addres": ["Shovot", "Urganch"],
    # "addres": "Urganch"
}

inson.update(
    {
    'lavozim': "Dasturchi", 
    "tajriba": 2,
    'addres': "Shovot"
}
)
inson.pop("addres")
del inson['yosh']
inson.popitem()
# inson1 = inson.copy()
# del inson
inson1 = inson.copy()
inson['yosh'] = 21
inson1['tajriba'] = 2
# print(inson1)


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

# print(myfamily['child3']['name'])


keys = ['Ten', 'Twenty', 'Fourty']
values = [10, 20, 40, 30]

dict1 = dict(zip(keys, values))

# print(dict1)




# for i in inson:
#     print(inson[i])

# for i, j in inson.items():
#     print(i, j)



# print(inson.keys())
# print(inson.values())
# print(inson.items())

# if "ism" in inson:
#     print(inson['ism'])
# else:
#     print("Kalit so'z topilmadi")

# inson['yosh'] = 22
# print(inson["millat1"])
# print(inson.get("millat"))






# n = input("Kalitni kiriting: ")
# print(len(inson))
# l = inson['addres']
# inson['addres'][1] = "Toshkent"
# l.append("Buxoro")
# l.remove("Toshkent")
# print(inson['addres'])


thisdict = {
    "quiz": {
        "sport": {
            "q1": {
                "question": "Which one is correct team name in NBA?",
                "options": [
                    "New York Bulls",
                    "Los Angeles Kings",
                    "Golden State Warriros",
                    "Huston Rocket"
                ],
                "answer": "Huston Rocket"
            }
        },
        "maths": {
            "q1": {
                "question": "5 + 7 = ?",
                "options": [
                    "10",
                    "11",
                    "12",
                    "13"
                ],
                "answer": "12"
            },
            "q2": {
                "question": "12 - 8 = ?",
                "options": [
                    "1",
                    "2",
                    "3",
                    "4"
                ],
                "answer": "4"
            }
        }
    }
}

# print(thisdict['quiz']['maths']['q2']['answer'])