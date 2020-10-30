import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import pdfkit

url = 'https://epaper.eenadu.net/Home/Index?date=24/10/2020&eid=3&pid=1167104'



res = requests.get(url).content
soup = BeautifulSoup(res, 'html.parser')

formatted_text = soup.prettify()
#print(formatted_text)

config = pdfkit.configuration(wkhtmltopdf="C:\Program Files\wkhtmltopdf\bin")
pdfkit.from_url(url,configuration=config)
print('sucess....!')