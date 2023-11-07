import requests
r=requests.get("https://quotes.toscrape.com")
text=r.text
with open("quotes.txt", "w") as file:
    pass
# with open("quotes.txt",'w') as f:
#     for line in text.split("\n"):
#         if '<span class="text" itemprop="text">' in line :
#             line=line.replace('<span class="text" itemprop="text">“','').replace('”</span>','').strip()
#             f.write(line)
#             f.write('\n')
with open ("quotes.txt",'w'):
    for line in text.split('\n'):
        if '<span>by <small class="author" itemprop="author">' in line :
            line=line.replace('<span>by <small class="author" itemprop="author">','').replace('</small>','').strip()
            print(line)