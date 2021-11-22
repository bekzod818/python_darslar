import requests

url = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/btc.json"


response = requests.get(url).json()
date = response['date']
uzs = response['btc']['uzs']
usd = response['btc']['usd']
rub = response['btc']['rub']
eur = response['btc']['eur']
kzt = response['btc']['kzt']
info = f"Bugun {date}\n1 BTC - {round(uzs, 2)} so'm\n1 BTC - {round(usd, 2)} dollar\n1 BTC - {round(eur, 2)} evro\n1 BTC - {round(rub, 2)} rubl\n1 BTC - {round(kzt, 2)} tanga."

print(info)