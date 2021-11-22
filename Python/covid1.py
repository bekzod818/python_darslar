from covid import Covid

covid = Covid()
countries = covid.list_countries()
# print(len(countries))

for i in range(len(countries)):
    if countries[i]['name'].lower() == "uzbekistan":
        print(countries[i])

uzb_cases = covid.get_status_by_country_id(189)
print(uzb_cases)