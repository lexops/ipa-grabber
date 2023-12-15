from bs4 import BeautifulSoup
from lxml import etree
import requests

word = input("Search word: ")

url = f"https://dictionary.cambridge.org/dictionary/english-portuguese/{word}"

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, "html.parser")
dom = etree.HTML(str(soup)) 

result = dom.xpath('//*[@id="dataset-caldpt"]/div[2]/div[2]/div/span/div/span/div/span[2]/span[2]/span')

if len(result) < 1:
    print(f"\"{word}\" not found. Please, check your spelling.")
else:
    print(result[0].text)