friend = {
    'first_name': 'javlon',
    'last_name': "ro'zimov",
    'age': 20,
    'city': 'urgench'
}
full_name = friend['first_name'] + " " + friend['last_name']
print(f"{full_name.title()} {friend['age']} da {friend['city'].title()}da yashaydi.")
football = {
    'ronaldo': 7,
    'messi': 10,
    'neymar': 11,
    'holland': 19,
    'mbappe': 29,
    'lewandowski': 9
}
for x, y in football.items():
    print(f"{x.title()}ning sevimli raqami {y}.")

python = {
    'int': 'butun sonlar',
    'float': 'haqiqiy sonlar',
    'str': 'string tipi',
    'if': 'agar',
    'elif': 'aks-holda agar',
    'else': 'aks-holda'
}
for x, y in sorted(python.items()):
    print(f"{x} -> {y}")
