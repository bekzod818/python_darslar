import requests
from bs4 import BeautifulSoup as Bs

base_url = "https://www.transfermarkt.com"
extra_url = "/uefa-champions-league/torschuetzenliste/pokalwettbewerb/CL"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

rating = []

response = requests.get(base_url + extra_url, headers=headers)

html = response.text

html_rating = Bs(html, 'html.parser')

players = html_rating.select('div.responsive-table table > tbody > tr > td:last-child')

for player_row in players:
    player = player_row.select_one("a")
    name = player.attrs['title']
    goalscore = int(player.text)
    rating.append((name, goalscore))

print(response.status_code, "status code")
print(rating)
