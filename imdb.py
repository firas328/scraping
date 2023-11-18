import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

req=requests.get(url,headers=headers)
print(req.status_code)
html=req.text
soop=BeautifulSoup(html,'html.parser')
items=soop.find('ul',{'class':'ipc-metadata-list ipc-metadata-list--dividers-between sc-9d2f6de0-0 iMNUXk compact-list-view ipc-metadata-list--base','role':'presentation'})
lis=items.findAll('li')
with open ("imdb.csv",'w',encoding='utf-8') as f:
    for li in lis:
        #get ths url of the movie description
        urlMovie="https://www.imdb.com"+li.find('a')['href']
        re=requests.get(urlMovie,headers=headers)
        soop=BeautifulSoup(re.text,'html.parser')
        #get the classes of the movie 
        classes=list(map(lambda x:x.span.string.strip() ,soop.find('div',{'class':'ipc-chip-list__scroller'}).findAll('a')))
        #get general informations of the movie 
        name=li.find('h3',{'class': 'ipc-title__text'}).string
        rating, votes=li.find('span',{'class':'ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating'}).text.strip().split()
        votes=votes.replace('(','').replace(')','')
        #here the third attribute some time is null so we passe it
        year,duration,*_= map(lambda x:x.string, li.find('div',{'class':'sc-479faa3c-7 jXgjdT cli-title-metadata'}) )
        classes=";".join(classes)
        f.write(name.replace(',',' ')+','+year+','+votes+','+year+','+duration+','+classes)
        f.write('\n')

