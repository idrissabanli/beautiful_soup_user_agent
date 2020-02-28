from bs4 import BeautifulSoup
import requests


class Scraper():
    url = 'https://www.kadr-az.info/bos-vakansiyalar/29910-proqramci'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}
    def __init__(self):
        response = requests.get(self.url, headers=self.headers)
        self.soup = BeautifulSoup(response.content, 'html.parser')

    def get_requirements(self):
        html_elements = self.soup.select('div.description > dd:nth-child(2) > p')
        return ''.join([x.text for x  in html_elements]).replace('[email protected]', self.get_email())

    def decode_email(self, e):
        de = ""
        k = int(e[:2], 16)
        for i in range(2, len(e)-1, 2):
            de += chr(int(e[i:i+2], 16)^k)
        return de

    def get_email(self):
        email_element = self.soup.select_one('div.description .__cf_email__')
        self.email = self.decode_email(email_element.get('data-cfemail', None)) if email_element else ''
        
        return self.email


if __name__ == '__main__':
    scraper = Scraper()
    print(scraper.get_requirements())
