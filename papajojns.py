import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.papajohns.by/menyu/pizza")
soup = BeautifulSoup(r.text, features="html.parser")
data = soup.find("div", {"class": "b-page__main"}).find("noscript")
ass = data.findAll("a")
arr = []
for cost in data.findAll("p"):
    if cost.text != "":
        arr.append(cost.text)
if len(ass) == len(arr):
    print("true")
else:
    print("false")
    print (len(ass))
    print (ass)
    
for pizza in list(zip(ass, arr)):
    print(pizza[0].text)
    print(pizza[1])
    print("-----")
