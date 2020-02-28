from bs4 import BeautifulSoup
import requests


class Scraper():
    def __init__(self):
        response = requests.get('https://www.kadr-az.info/bos-vakansiyalar/29942-texniki-mutexessis', headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'})
        self.soup = BeautifulSoup(response.content, 'html.parser')

    def get_requirements(self):
        return self.soup.select('div.description > dd:nth-child(2) > p')


if __name__ == '__main__':
    scraper = Scraper()
    print(scraper.get_requirements())
