import requests

url = requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/kzt/uzs.json").json()

print(round(url['uzs'], 2), "so'm")