"""
def katta_harf(matnlar):    
    for i in range(len(matnlar)):
        matnlar[i] = matnlar[i].title()

ismlar = ['ali', 'vali', 'hasan', 'husan']
katta_harf(ismlar)
print(ismlar)

# def katta_harf(matnlar):
#     l = []
#     while matnlar:
#         matn = matnlar.pop()
#         l.append(matn.title())
#     l.reverse()
#     return l
def katta_harf(matnlar):
    matnlar = matnlar[:]
    for i in range(len(matnlar)):
        matnlar[i] = matnlar[i].title()
    return matnlar

ismlar = ['ali', 'vali', 'hasan', 'husan']
yangi_ismlar = katta_harf(ismlar[:])
print(ismlar)
print(yangi_ismlar)
"""
def bahola(ismlar):
    ismlar = ismlar[:]
    baholar = {}
    for ism in ismlar:
        baho = input(f"{ism.title()}ning bahosi: ")
        baholar[ism] = baho
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)
print(talabalar)