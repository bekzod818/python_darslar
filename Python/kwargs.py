def avto_info(kompaniya, model, **data):
    data['company'] = kompaniya
    data['model'] = model
    return data

cars1 = avto_info('GM', 'Malibu', rang='Qora', korobka = 'Mexanik')
print(cars1)

avto2 = avto_info("Kia", "K5", rang='qizil', narh=34000)
print(avto2)

cars2 = avto_info('')