import requests

with open("quotes.csv", "w") as file:
    pass
for i in range(1,11):
    r=requests.get(f"https://quotes.toscrape.com/page/{i}")
    text=r.text
    print(r.status_code)
    with open ("quotes.csv",'a',encoding='utf-8') as f:
        # for line in text.split('\n'):
        #     if '<span>by <small class="author" itemprop="author">' in line :
        #         line=line.replace('<span>by <small class="author" itemprop="author">','').replace('</small>','').strip()
        #         f.write(line)
    
        # for line in text.split("\n"):
        #     if '<span class="text" itemprop="text">' in line :
        #         line=line.replace('<span class="text" itemprop="text">“','').replace('”</span>','').strip()
        #         f.write(line)
        #         f.write('\n')
        for line in text.split('\n'):
            if  '<span class="text" itemprop="text">' in line :  
                quotes=line.replace('<span class="text" itemprop="text">“','').replace('”</span>','').strip()   
          
            
            if '<span>by <small class="author" itemprop="author">' in line :
                author=line.replace('<span>by <small class="author" itemprop="author">','').replace('</small>','').replace(",","|").strip()
                f.write(author+","+quotes)
                f.write("\n")                  
              
            
