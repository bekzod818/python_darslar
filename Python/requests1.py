import requests
from bs4 import BeautifulSoup

url = "http://bekzod7.uz/"

html = requests.get(url).text

soup = BeautifulSoup(html, 'html.parser')

div = soup.find_all('div', class_="badge")

print(soup.h1.text, div[0].text, sep="")
