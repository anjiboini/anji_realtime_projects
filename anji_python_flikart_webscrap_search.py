import requests
from bs4 import BeautifulSoup
import pandas as pd
import json



#keyword = 'phones under 10000'
keyword = input('Enrer Keyword : ')
url = 'https://www.flipkart.com/search?q='+keyword+''

res = requests.get(url).content
#print(res)
soup = BeautifulSoup(res,'html')
#print(soup)

print('#----------------------------Top Results for '+keyword+'------------------------#')
#.........Vertical data....................
data = soup.find_all('div', class_='_3wU53n')
#print(data.text)
c=1
for item in data:
    print(c,item.text)
    c+=1
#.........Horizintal data....................
data = soup.find_all('a', class_='_2cLu-l')
#print(data.text)
c=1
for item in data:
    print(c,item.text)
    c+=1


