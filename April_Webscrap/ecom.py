import requests
import pandas as pd
from bs4 import BeautifulSoup
response=requests.get("https://sportscorner.qa/en/mens/footwear.html?brand=5662")
print(response)

soup=BeautifulSoup(response.content,'html.parser')
#print(soup)

names =soup.find_all('a',class_ = 'product-item-link')
#print(names)
name=[]
for i in names[1:10]:
    d=i.get_text(strip=True)
    # d=d.rstrip()
    name.append(d)
print(name)
prices=soup.find_all('span',class_='price')
#print(prices)
price=[]
for i in prices[1:10]:
    d=i.get_text(strip=True)  
    d = d.replace('QR','').replace('\xa0','').strip()
    price.append(float(d))
print(price)
df=pd.DataFrame()
df['Names']=name
df['price']=price
print(df)
df.to_csv("shoes.csv")