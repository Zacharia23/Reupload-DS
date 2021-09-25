import requests
from bs4 import BeautifulSoup

URL = "https://covid.rahisiweb.co.tz/"
page = requests.get(URL)

# print(page.text)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all("div", class_="hidden-sm hidden-xs text-center")
print(results.prettify())
