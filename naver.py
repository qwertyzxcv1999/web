import requests
from bs4 import BeautifulSoup

req = requests.get('https://comic.naver.com/webtoon/list.nhn?titleId=183559&weekday=mon&page=1')
soup=BeautifulSoup(req.text,'html.parser') 
s=soup.find_all('div',{'class':'detail'})

a=1
for i in s:
    name=i.text
    name1=name.strip
    print(name[13:20])
    a=a+1