from bs4 import BeautifulSoup
import requests

with open("BS4quotes.csv","a",encoding="utf-8") as f:
    for i in range(1,11):
        req=requests.get(f"https://quotes.toscrape.com/page/{i}")
        print(req.status_code)
        html=req.text
        html=BeautifulSoup(html,"html.parser")
        for tag in html.find_all('small',{'class','author'}):
            f.write(tag.string)
            f.write('\n')
            

