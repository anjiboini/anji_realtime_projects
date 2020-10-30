import requests
from bs4 import BeautifulSoup
import pandas as pd
import json


#url = 'https://www.flipkart.com/search?q=laptop'

url = "https://www.flipkart.com/search?q=laptop"
res = requests.get(url).content
soup = BeautifulSoup(res, 'html.parser')
#print(soup.prettify())
titles = soup.find_all('div',class_='_3wU53n')
ratings = soup.find_all('div',class_='hGSR34')
reviews = soup.find_all('span',class_='_38sUEc')
prices = soup.find_all('div',class_='_1vC4OE')
specs = soup.find_all('div',class_='_3ULzGw')
images = soup.find_all('div',class_='_3BTv9X')



mlink = []
for link in soup.find_all('a',class_='_31qSD5'):
    links = (link.get('href'))
    mlink.append('https://www.flipkart.com' + links)

mobiles = []
m_ratings = []
m_reviews = []
m_prices = []
m_specs = []


#c=1
for title,rating,review,price,spec in zip(titles,ratings,reviews,prices,specs):

    #print(title.text,rating.text,review.text,price.text)

    mobiles.append(title.text)
    m_ratings.append(rating.text)
    m_reviews.append(review.text)
    m_prices.append(price.text)
    m_specs.append(spec.text)

  #  c+=1

#print(mobiles)
#print(m_ratings)
#print(m_reviews)
#print(m_prices)

# Exporting to csv files

data = {'Laptops':mobiles,'Ratings':m_ratings,'Reviews':m_reviews,'Prices':m_prices,'Specs':m_specs,'Links':mlink}
#print(data)

df = pd.DataFrame(data=data)
#print(df.head())
df.to_excel('laptop_data.xlsx', index=False)
print(df)





'''

#df.to_csv('mobile_data.csv',index=False)
#print('Success')

# Export to json fomat
d = json.dumps(data)
print(d)

l = json.loads(d)
with open('mobile_data.json', 'w') as f:
    f.write(d)
    f.close()

print('Success.....!')

'''