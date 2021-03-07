# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup

f = open('test.txt', 'w+', encoding='utf-8')
url = "https://groups.google.com/g/tw.bbs.rec.marvel/c/1vE6dRO7Jog"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find('div',class_='ptW7te').p

for result in results:
    f.write(str(result)+"\n")
    print(result)
f.close()
