import requests
from bs4 import BeautifulSoup

req = requests.get('https://comic.naver.com//webtoon/list.nhn?titleId=694807&weekday=mon')
soup=BeautifulSoup(req.text,'html.parser') 
titlename=soup.find_all("td",{'class':'title'})
star=soup.select('div.rating_type > strong')

a=0
starpoint=star[a]
print(starpoint.text)
for i in titlename:
    
    print(i.text,starpoint.text,end='')
    a=a+1

    #content > table > tbody > tr:nth-child(3) > td:nth-child(3) > div > strong