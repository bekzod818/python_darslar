# import requests
# from bs4 import BeautifulSoup

# url = "https://glotr.uz/noutbuki/proizvoditel-acer/linejka-processora-core-i3-core-i5-core-i7-core-i9/"

# html = requests.get(url).text

# soup = BeautifulSoup(html, "html.parser")

# div = soup.findAll("div", attrs={"class":"proposals-item-content"})[13]
# name = div.find('a', attrs={'class': ['proposal-img', 'lazyload']})
# link = name.attrs['data-src']

# div_info = soup.findAll("div", attrs={"class": "proposal-main-info-wrap"})[13]
# name_href = div.find("a", attrs={"class": "proposal-item-link"})
# span = name_href.select("span")
# name = span[0].text

# div_price = soup.findAll("div", attrs={"class": ["proposal-price_wrap", "text-overflow"]})[13]
# href = div_price.find("div", attrs={"proposal-main-price"})
# price = href.select("span.proposal-price-value")[0].text
# valyuta = href.select("span.proposal-price-currency")[0].text

# print(name, link, price, valyuta)

import requests
from bs4 import BeautifulSoup

url = "https://glotr.uz/noutbuki-v-taskente/proizvoditel-apple/"

html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")

div = soup.findAll("div", attrs={"class":"proposals-item-content"})[5]
name = div.find('a', attrs={'class': ['proposal-img', 'lazyload']})
link = name.attrs['data-src']
about = "https://glotr.uz" + name.attrs['href']

div_info = soup.findAll("div", attrs={"class": "proposal-main-info-wrap"})[5]
name_href = div.find("a", attrs={"class": "proposal-item-link"})
span = name_href.select("span")
name = span[0].text

div_price = soup.findAll("div", attrs={"class": ["proposal-price_wrap", "text-overflow"]})[5]
href = div_price.find("div", attrs={"proposal-main-price"})
price = href.select("span.proposal-price-value")[0].text
valyuta = href.select("span.proposal-price-currency")[0].text

print(name, link, price + valyuta)
print(about)