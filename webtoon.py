import requests
from bs4 import BeautifulSoup

a="1"
b="https://comic.naver.com/webtoon/detail.nhn?titleId=316909&no="
c=b+a
req = requests.get(c)
d=int(a)
while d<248 :
    c=b+a
    req = requests.get(c)
    soup=BeautifulSoup(req.text,'html.parser') 
    s=soup.select("div.view > h3")
    star=soup.find("span",attrs={"id":"topPointTotalNumber"})
    for i in s:

        print(a,"화",i.text,"평점",star.text)
        d=int (a)
        d=d+1
        a=str (d)
