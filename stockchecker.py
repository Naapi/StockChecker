import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(c)
url = 'https://finance.yahoo.com/quote/AAPL/'
data = requests.get(url)
jsoni = data.json()
print(data.text)
