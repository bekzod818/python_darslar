import requests
from bs4 import BeautifulSoup

url = "https://en.soccerwiki.org/league.php?leagueid=28"

html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")

# print(soup.prettify())
# print(soup.h2)
# print(soup.h2.text)

div = soup.find_all('div', class_="factfileBorder")[1]

table = div.find('table', attrs={'class': ['no-arrow', 'tabledata']})

td_s = table.select('td.team:nth-child(2)')

print('_*' * 10)

for td in td_s:
    print(td.find('a').text)

print('_*' * 10)