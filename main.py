import requests
from bs4 import BeautifulSoup

for page in range(6, 79):  # page
    f = open("output//test_" + str(page).zfill(2), 'w+')
    url = "https://ben1998.com/articles/" + str(page)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
    }
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('div', class_='entry-content')
    for result in results:
        f.write(str(result.text.strip()))
        print(result.text.strip())
    f.close()
