import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
name= requests.get(url)
soup = BeautifulSoup(name.text,"lxml")
name1 = soup.find_all("a",class_ = "title")
#print(name1)
product_name = []
for data1 in name1:
  num1 = data1.text
  product_name.append(num1) 
#print(product_name)
name2 = soup.find_all("h4",class_ = "float-end")
price_name = []
for data2 in name2:
  num2 = data2.text 
  price_name.append(num2)
print(price_name)
name3 = soup.find_all("p", class_ = "description")
describe_name = []
for data3 in name3:
   num3 = data3.text 
   describe_name.append(num3)
#print(describe_name)

name4 = soup.find_all("p",class_  = "float-end")
review_name = []
for data4 in name4:
    num4 = data4.text 
    review_name.append(num4)
print(review_name)
