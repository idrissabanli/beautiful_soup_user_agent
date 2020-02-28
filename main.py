from bs4 import BeautifulSoup
import requests


response = requests.get('https://www.kadr-az.info/bos-vakansiyalar/29942-texniki-mutexessis', headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'})

print(response)
soup = BeautifulSoup(response.content, 'html.parser')

print(soup.select('div.description > dd:nth-child(2) > p'))
