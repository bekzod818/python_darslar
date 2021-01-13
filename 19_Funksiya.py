def salom_ber(ism):
    """Salom beruvchi funksiya"""
    print(f'Assalomu aleykum {ism.title()}')
salom_ber('Bekzod')
#print(salom_ber.__doc__)

def full_name(first_name, last_name):
    full = first_name + " " + last_name
    print(full)
full_name(last_name = 'Raximov', first_name = 'Bekzod')

def yosh_hisobla(tugilgan_yil, joriy_yil = 2020):
    print(f'Siz {joriy_yil - tugilgan_yil} yoshdasiz.')
yosh_hisobla(2000)
yosh_hisobla(1995, 2020)