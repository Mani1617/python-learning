import pandas as pd
import requests
from bs4 import BeautifulSoup
response=requests.get('https://books.toscrape.com/')
print(response)
soup=BeautifulSoup(response.content,'html.parser')
print(soup)
names=soup.find_all('h3')
# print(names)
book_name=[]
for i in names[1:11]:
    d = i.a['title']
    book_name.append(d)
print(book_name)

prices=soup.find_all('p',class_='price_color')
price = []

for i in prices[1:11]:
    price.append(float(i.text[1:]))

print(price)

df=pd.DataFrame()
df['Book_Name']=book_name
df['Prices']=price
print(df)
df.to_csv("Books.csv")


