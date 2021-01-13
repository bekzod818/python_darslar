"""
def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism] = int(baho)
    return baholar
talabalar = ['hasan', 'olim', 'azim', 'husan', 'ali']
baholar = bahola(talabalar[:])
print(baholar)
print(talabalar)
"""
def tel_raqam(ismlar):
    nomerlar = {}
    while ismlar:
        ism = ismlar.pop()
        nomer = input(f"{ism.title()}ning telefon raqamani kiriting: ")
        nomerlar[ism] = nomer
    return nomerlar
gruppodoshlo = ['mustafo', 'sherzod', 'maqsad', 'javlon', 'doniyor']
nomerlar = tel_raqam(gruppodoshlo)
print(nomerlar)