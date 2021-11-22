import json

# dump, dumps, load, loads

with open("weather.json") as file:
    data = json.load(file)

print(f"Bugungi ob-havo {round(data['main']['temp'] - 273, 2)} C")
print(f"Bugungi bosim {data['main']['pressure']} MPa")
print(f"Bugungi namlik {data['main']['humidity']}%")