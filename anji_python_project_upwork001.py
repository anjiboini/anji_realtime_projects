import requests
from bs4 import BeautifulSoup
import pandas as pd
import json



url = 'https://flipdocs.com/'

res = requests.get(url).content
soup = BeautifulSoup(res, 'html.parser')

images = soup.find_all('div',class_='owl-item active')

print(images)
#for img in images:
 #   print(img['src'])
