import requests
from bs4 import BeautifulSoup as bs
import sys

url = 'https://www.dictionary.com/browse/'
word=sys.argv[1]
url+=word
print("\nWord : "+word)
try:
    data = requests.get(url)
    soup =bs(data.content,'html.parser')
except:
    print("Not Internet....")
    exit(-1)
posl = []
try:
    for pos in soup.find_all('span',{'class':'luna-pos'}):
        posl.append(pos)
    print("\nPart of Speech\n"+posl[0].get_text())
except:
    print("Word not found...")
    exit(0)
definitions = []

try:
    for defi in soup.find_all('div',{'value':'1'}):
        definitions.append(defi.text)
    print("\nDefinition\n"+definitions[0]+"\n")
except :
    print("Definition not found..")
