import requests
from bs4 import BeautifulSoup

mon="https://comic.naver.com/webtoon/weekdayList.nhn?week=mon"
req = requests.get(mon)
soup1=BeautifulSoup(req.text,'html.parser') 


s=soup1.find_all('a',{'class':'tit'})
s=set(s)
s=list(s)
k=soup1.select( 'dl > dt > a')
k=set(k)
k=list(k)

a=0
star=soup1.find("span",attrs={"id":"topPointTotalNumber"})

for link in k:
    
    asd=link.get('href')
    webtoon='https://comic.naver.com'+asd
    req1=requests.get(webtoon)
    soup2=BeautifulSoup(req1.text,'html.parser')
    titlename=soup2.find_all("td",{'class':'title'})
    star=soup2.select('div.rating_type > strong')
    nameofwebtoon=soup2.find_all('div',{'class':'detail'})
    for i in nameofwebtoon:
        name=i.text
        print(name[13:20])
    
    
   
    
    for i in titlename:
        starpoint=star[a]
        print(i.text,starpoint.text)
        if a <8:
            a=a+1 



   
#realTimeRankFavorite > li.rank01 > a
#content > div.list_area.daily_img > ul > li:nth-child(1) > dl > dt > a
#content > div.list_area.daily_img > ul > li:nth-child(1) > dl > dt > a
#content > div.list_area.daily_img > ul > li:nth-child(1) > dl > dt > a
#content > div.list_area.daily_img > ul > li:nth-child(2) > dl > dt > a
#content > div.list_area.daily_img > ul > li:nth-child(1) > div > a
#content > div.list_area.daily_img > ul > li:nth-child(1) > div > a
#content > div.list_area.daily_img > ul > li:nth-child(1) > div > a
