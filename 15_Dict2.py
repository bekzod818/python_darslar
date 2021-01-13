python = {
    'int': 'butun sonlar',
    'float': 'Haqiqiy sonlar',
    'complex': 'Kompleks sonlar',
    'str': 'Matn yoki harflar',
    'if': 'Shart operatori',
    'for': 'Takrorlanuvchi operator',
    'bool': 'Mantiqiy qiymat qaytaradi',
    'list': 'Ro\'yhat',
    'tuple': 'Kortej',
    'dict': 'Lug\'at'
}
for x in sorted(python.keys()):
    print(f"{x} => {python[x]}")
    