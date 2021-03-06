# -*- coding: UTF-8 -*-
import time
import requests
from bs4 import BeautifulSoup

start = time.time()
f = open("output_other/test_01.txt", 'w+', encoding="utf-8")
url = "http://web.archive.org/web/20100515002140/http://mypaper.pchome.com.tw/fld/post/1241491918"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
}
page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('div', class_='text_01')

for result in results:
    result = result.text.strip()
    f.write(result)
f.close()

i = 2
while i <= 30: # Put times
    f = open("output_other\\test_" + str(i).zfill(2) + ".txt", 'w+', encoding="utf-8")
    next_one = soup.find('div', class_='datediv').find_all('a')[1]['href']
    print(next_one)
    url = "http://web.archive.org" + next_one
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find_all('div', class_='text_01')
    for result in results:
        result = result.text.strip()
        f.write(result)
    f.close()
    i += 1

print('花費: %f 秒' % (time.time() - start))

# clear empty line
# fr = open("test", 'r', encoding="utf-8")
# fn = open("test_1", 'w', encoding="utf-8")
# for line in fr.readlines():
#     if line.split():
#         fn.writelines(line)
#     else:
#         fn.writelines("")
# fr.close()
# fn.close()
