import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.papajohns.by/menyu/pizza")
soup = BeautifulSoup(r.text, features="html.parser")
data = soup.findAll("div", {"class": "b-page__main"})
ass = data[0].findAll("a")
for pizza in ass:
    if "/menyu/pizza" in str(pizza) and "<nobr>" not in str(pizza):
            print(pizza.text)
