def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = int(input(f"Talaba {ism}ning bahosini kiriting: "))
        baholar[ism] = baho
    return baholar

talabalar = ['Behruz', 'Shohmalik', 'Amirbek', 'Javohir', 'Mirjamol']
baholar = bahola(talabalar)
print(baholar)