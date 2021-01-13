'''
prompt = 'Please enter the name of a city you have visited:'
prompt += "\n(Enter 'quit' when you are finished): "
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to " + city.title() + '!')

unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f'Verifying user: {current_user.title()}')
    confirmed_users.append(current_user)
print('\nThe following users have been confirmed:')
for user in confirmed_users:
    print(f'{user.title()}')

pets = ['cat', 'dog', 'goldfish', 'cat', 'rabbit', 'dog', 'cat']
while 'cat' in pets:
    pets.remove('cat')
print(pets)

responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes / no) ")
    if repeat == 'no':
        polling_active = False
    
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

'''
sayohatlar = {}
ishora = True
while ishora:
    ism = input("\nIsmingiz nima? ")
    shahar = input("Qaysi shaharga sayohat qilmoqchisiz? ")
    sayohatlar[ism] = shahar

    takror = input("Yana malumot qiritishni hohlaysizmi? (ha / yo'q) ")
    if takror == "yo'q":
        ishora = False
print("\n<---- Sayohatchilar ---->")
for ism, shahar in sayohatlar.items():
    print(f"{ism} {shahar}ga sayohat qilmoqchi.")